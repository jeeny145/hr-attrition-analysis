import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df = df.drop(columns=["EmployeeCount", "Over18", "StandardHours"])
    return df
def generate_insights(df):
    insights = {}
    
    overtime_attrition = df.groupby("OverTime")["Attrition"].value_counts(normalize=True).unstack()
    insights["overtime_attrition"] = overtime_attrition
    
    dept_attrition = df.groupby("Department")["Attrition"].value_counts(normalize=True).unstack()
    insights["department_attrition"] = dept_attrition
    
    income_by_attrition = df.groupby("Attrition")["MonthlyIncome"].mean()
    insights["income_by_attrition"] = income_by_attrition
    
    satisfaction_by_attrition = df.groupby("Attrition")["JobSatisfaction"].mean()
    insights["satisfaction_by_attrition"] = satisfaction_by_attrition
    
    return insights
import matplotlib.pyplot as plt
import os

def save_charts(df, output_dir="../outputs/charts"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Chart 1: OverTime vs Attrition
    df.groupby("OverTime")["Attrition"].value_counts(normalize=True).unstack().plot(kind="bar")
    plt.title("Attrition Rate by OverTime Status")
    plt.ylabel("Proportion")
    plt.savefig(f"{output_dir}/overtime_attrition.png", bbox_inches="tight")
    plt.close()
    
    # Chart 2: Department vs Attrition
    df.groupby("Department")["Attrition"].value_counts(normalize=True).unstack().plot(kind="bar", figsize=(8,5), color=["#2E86AB", "#E67E22"])
    plt.title("Attrition Rate by Department", fontsize=13, fontweight="bold")
    plt.ylabel("Proportion")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/department_attrition.png", bbox_inches="tight")
    plt.close()
    
    # Chart 3: Income vs Attrition
    df.groupby("Attrition")["MonthlyIncome"].mean().plot(kind="bar", figsize=(6,5), color=["#2E86AB", "#E67E22"])
    plt.title("Average Monthly Income: Stayed vs Left", fontsize=13, fontweight="bold")
    plt.ylabel("Average Monthly Income")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/income_attrition.png", bbox_inches="tight")
    plt.close()
    
    # Chart 4: Satisfaction vs Attrition
    df.groupby("Attrition")["JobSatisfaction"].mean().plot(kind="bar", figsize=(6,5), color=["#2E86AB", "#E67E22"])
    plt.title("Average Job Satisfaction: Stayed vs Left", fontsize=13, fontweight="bold")
    plt.ylabel("Average Job Satisfaction (1-4)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/satisfaction_attrition.png", bbox_inches="tight")
    plt.close()
    
    print("Charts saved successfully!")

def main():
    print("Starting HR Attrition Analysis Pipeline...\n")
    
    # Step 1: Load and clean data
    df = load_and_clean_data("../data/raw/hr_data.csv")
    print(f"Data loaded: {df.shape[0]} rows, {df.shape[1]} columns\n")
    
    # Step 2: Generate insights
    insights = generate_insights(df)
    print("Key Insights:")
    print("\nOverTime vs Attrition:")
    print(insights["overtime_attrition"])
    print("\nDepartment vs Attrition:")
    print(insights["department_attrition"])
    print("\nAverage Income by Attrition:")
    print(insights["income_by_attrition"])
    print("\nAverage Satisfaction by Attrition:")
    print(insights["satisfaction_by_attrition"])
    
    # Step 3: Save charts
    print("\nGenerating charts...")
    save_charts(df)
    
    print("\nPipeline completed successfully!")


if __name__ == "__main__":
     main()