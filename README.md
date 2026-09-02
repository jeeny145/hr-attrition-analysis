# HR Attrition Analysis & Prediction

Analysis of employee attrition patterns using the IBM HR Analytics dataset, 
with statistical testing and a predictive model to identify at-risk employees.

## Problem Statement
Employee attrition costs companies significant time and money in hiring and 
training. This project analyzes what factors drive attrition and builds a 
model to flag employees at higher risk of leaving.

## Project Structure
data/ - raw and processed datasets
notebooks/ - exploration, analysis, and modeling notebooks
scripts/ - automated data pipeline
outputs/ - charts and generated reports

## Tools Used
- Python (Pandas, NumPy, Matplotlib, Scikit-learn, SciPy)
- SQL (SQLite)
- Jupyter Notebook

## Key Steps
1. Data cleaning and preprocessing
2. Exploratory data analysis
3. Statistical hypothesis testing
4. Predictive model (Logistic Regression)
5. Automated reporting pipeline

## Key Findings

**1. Overtime is the strongest predictor of attrition**
Employees who work overtime leave at nearly 3x the rate of those who don't 
(30.5% vs 10.4%).

![Overtime vs Attrition](outputs/charts/overtime_attrition.png)

**2. Sales and HR see higher attrition than R&D**
Sales (~20.6%) and HR (~19%) have noticeably higher attrition rates 
compared to Research & Development (~13.8%).

![Department vs Attrition](outputs/charts/department_attrition.png)

**3. Lower income correlates with higher attrition**
Employees who left had an average monthly income of ₹4,787 compared to 
₹6,833 for those who stayed.

![Income vs Attrition](outputs/charts/income_attrition.png)

**4. Job satisfaction has a smaller but present effect**
Employees who left reported slightly lower average job satisfaction 
(2.47 vs 2.78 on a 4-point scale) — a smaller gap than overtime or income.

![Satisfaction vs Attrition](outputs/charts/satisfaction_attrition.png)

## Statistical Validation

A Chi-square test of independence was conducted to verify whether OverTime 
and Attrition are meaningfully related, rather than the pattern occurring 
by chance.

- Chi-square statistic: 87.56
- P-value: < 0.001

The result is highly statistically significant (p < 0.05), confirming that 
employees who work overtime are significantly more likely to leave the 
company. This is not a coincidental pattern in the data.

A second Chi-square test examined the relationship between Department and 
Attrition.

- Chi-square statistic: 10.80
- P-value: 0.0045

This relationship is also statistically significant (p < 0.05), though 
notably weaker than the OverTime relationship (chi-square: 87.56). This 
suggests OverTime is a stronger driver of attrition than Department alone.

## Model Performance

A Logistic Regression model was trained to predict employee attrition.

- Accuracy: 89.5%
- Precision: 70%
- Recall: 36%

Note: Given the class imbalance in the dataset (only ~16% attrition), 
accuracy alone is not a reliable metric — a model predicting "No" for 
everyone would still score ~84%. The low recall (36%) indicates the model 
misses a majority of employees who actually leave, which limits its 
practical use for proactive HR intervention without further tuning 
(e.g., class balancing techniques like SMOTE, or adjusting the decision 
threshold).

## How to Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_exploration.ipynb
```

## Author
Your Name — [https://github.com/jeeny145]

