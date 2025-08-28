import streamlit as st
import pandas as pd
import plotly.express as px

# ==============================
# Page Config
# ==============================
st.set_page_config(page_title="Sales Dashboard", page_icon="📊", layout="wide")

# ==============================
# Load Data
# ==============================
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard_ready.csv", parse_dates=["Order Date"])
    return df

df = load_data()

# ==============================
# Sidebar Filters
# ==============================
st.sidebar.header("🔎 Filters")

region_filter = st.sidebar.multiselect(
    "Select Region", options=df["Region"].unique(), default=df["Region"].unique()
)

category_filter = st.sidebar.multiselect(
    "Select Category", options=df["Category"].unique(), default=df["Category"].unique()
)

subcat_filter = st.sidebar.multiselect(
    "Select Sub-Category", options=df["Sub-Category"].unique(), default=df["Sub-Category"].unique()
)

# Apply filters
df_filtered = df[
    (df["Region"].isin(region_filter)) &
    (df["Category"].isin(category_filter)) &
    (df["Sub-Category"].isin(subcat_filter))
]

# ==============================
# KPIs
# ==============================
st.title("📊 Global Superstore Dashboard")

total_sales = df_filtered["Sales"].sum()
total_profit = df_filtered["Profit"].sum()
total_quantity = df_filtered["Quantity"].sum()
avg_discount = df_filtered["Discount"].mean()

col1, col2, col3, col4 = st.columns(4)

# Show KPIs
st.markdown("### Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("📈 Total Profit", f"${total_profit:,.0f}")
col3.metric("📦 Quantity Sold", f"{total_quantity:,}")
col4.metric("🏷️ Avg. Discount", f"{avg_discount:.2%}")


st.markdown("---")

# ==============================
# Charts
# ==============================

st.subheader("📈 Sales & Profit by Segment")

# Sales over time (Year, Month)
st.subheader("Sales Over Time")
sales_time = df_filtered.groupby(["Year", "Month"], as_index=False)["Sales"].sum()
fig_time = px.line(sales_time, x="Month", y="Sales", color="Year", markers=False, title="Monthly Sales Trend")
st.plotly_chart(fig_time, use_container_width=True)


st.subheader("🌍 Sales by Region")
region_fig = px.pie(
    df_filtered.groupby("Region")[["Sales"]].sum().reset_index(),
    names="Region", values="Sales",
    title="Sales Distribution by Region"
)
st.plotly_chart(region_fig, use_container_width=True)

# ==============================
# Top 5 Customers
# ==============================
st.markdown("---")
st.subheader("Segment and Customer Analysis")
col_seg, col_cust = st.columns(2)
with col_seg:
    segment_sales = df_filtered.groupby('Segment')['Sales'].sum().reset_index()
    fig_segment_sales = px.bar(
        segment_sales,
        x='Segment',
        y='Sales',
        title="Sales by Segment",
        labels={'Sales': 'Total Sales ($)', 'Segment': 'Customer Segment'},
        color='Segment',
        height=400
    )
    st.plotly_chart(fig_segment_sales, use_container_width=True)
with col_cust:
    top_customers = df_filtered.groupby('Customer Name')['Sales'].sum().nlargest(5).reset_index()
    fig_top_customers = px.bar(
        top_customers,
        x='Sales',
        y='Customer Name',
        orientation='h',
        title="Top 5 Customers by Sales",
        labels={'Sales': 'Total Sales ($)', 'Customer Name': 'Customer'},
        color='Sales',
        height=400
    )
    fig_top_customers.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_top_customers, use_container_width=True)

# ==============================
# Footer
# ==============================
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Plotly")
