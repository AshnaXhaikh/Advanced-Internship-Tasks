# Loan Default Risk Prediction with Business Cost Optimization

## Project Overview

This project aims to predict the likelihood of loan defaults using the **Home Credit Default Risk Dataset** and optimize the decision threshold based on **business cost analysis**. The goal is to reduce financial losses by minimizing the cost of false positives (approving risky loans) and false negatives (rejecting safe loans).

## Objective

* Predict whether a client will default on a loan.
* Handle imbalanced data effectively.
* Define business costs for misclassifications.
* Optimize model threshold to minimize total business cost.

## Dataset

* **Source:** Home Credit Default Risk Dataset
* **Train size:** 307,511 rows × 122 columns
* **Test size:** 48,744 rows × 121 columns
* **Target variable:** `TARGET` (0 = No default, 1 = Default)

## Approach

1. **Exploratory Data Analysis (EDA):**

   * Examine missing values, distributions, and correlations.
   * Understand the dataset and detect potential data issues.

2. **Data Cleaning & Preprocessing:**

   * Handle missing values through imputation or column removal.
   * Encode categorical features and scale numerical features.
   * Balance classes using upsampling of the minority class.

3. **Modeling:**

   * Train binary classification models:

     * Logistic Regression
     * CatBoost Classifier
   * Use automatic class balancing in CatBoost.
   * Adjust thresholds to minimize business costs.

4. **Business Cost Optimization:**

   * Define costs for false positives (FP) and false negatives (FN).
   * Evaluate models across thresholds to find the optimal cut-off.
   * Visualize cost vs. threshold curve for decision-making.

## Key Metrics

* Confusion Matrix (TN, FP, FN, TP)
* Precision, Recall, F1-score
* ROC-AUC
* **Custom Business Cost**

## Tools & Libraries

* Python 3.11
* pandas, numpy
* scikit-learn
* CatBoost
* matplotlib, seaborn

## Results

* Identified optimal threshold using business cost optimization.
* CatBoost achieved the best trade-off between recall of defaults and total cost.
* Visualizations illustrate the cost vs. threshold curve and confusion matrix at selected thresholds.

## How to Use

1. Clone the repository.
2. Install dependencies:

```bash
pip install pandas numpy scikit-learn catboost matplotlib seaborn
```

3. Run the notebook step by step:

   * EDA → Preprocessing → Model Training → Threshold Optimization → Evaluation.

## Conclusion

This project demonstrates how integrating **business costs** into model evaluation can improve decision-making in credit risk scenarios. Threshold tuning ensures a balance between financial loss and prediction performance.

---
