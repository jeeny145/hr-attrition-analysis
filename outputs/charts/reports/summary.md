# HR Attrition Analysis — Summary Report

## Objective
Identify the key factors driving employee attrition and assess whether a 
predictive model can help HR proactively flag at-risk employees.

## Dataset
IBM HR Analytics Employee Attrition dataset — 1,470 employees, 35 attributes 
including department, income, overtime status, and satisfaction scores.

## Key Findings

**1. Overtime is the single strongest driver of attrition.**
Employees working overtime leave at nearly 3x the rate of those who don't 
(30.5% vs 10.4%). This relationship is statistically significant 
(Chi-square = 87.56, p < 0.001).

**2. Department matters, but less than overtime.**
Sales (20.6%) and HR (19%) see higher attrition than R&D (13.8%). This 
relationship is also statistically significant (Chi-square = 10.80, 
p = 0.0045), but considerably weaker than the overtime effect.

**3. Lower-paid employees are more likely to leave.**
Employees who left earned an average monthly income of ₹4,787, compared to 
₹6,833 for those who stayed.

**4. Job satisfaction has a smaller effect.**
Employees who left reported slightly lower satisfaction (2.47 vs 2.78 on a 
4-point scale) — a modest gap compared to overtime or income.

## Predictive Model
A Logistic Regression model was built to flag at-risk employees. Two 
versions were compared:

| Metric    | Default Model | Balanced Model |
|-----------|---------------|-----------------|
| Accuracy  | 89.5%         | 71.4%           |
| Precision | 70.0%         | 25.8%           |
| Recall    | 36.0%         | 61.5%           |

The balanced model catches significantly more at-risk employees (61.5% vs 
36% recall) at the cost of more false positives — a reasonable trade-off 
for HR use cases where missing a flight-risk employee is costlier than an 
unnecessary check-in.

## Recommendations
1. **Review overtime policy** — the strongest and most actionable driver 
   of attrition identified in this analysis.
2. **Investigate Sales and HR department conditions** specifically, given 
   their elevated attrition rates.
3. **Use the balanced model for proactive flagging**, not as a sole 
   decision-maker — it should support, not replace, HR judgment.
   