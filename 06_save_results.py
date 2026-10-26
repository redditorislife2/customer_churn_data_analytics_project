# SAVE THE CLEANED DATA AND ANALYSIS TABLES
import sqlite3

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_DIR / "customers_cleaned.csv", index=False)

# Store the analysis-ready customer data in SQLite and calculate segment rates.
# This dataset is a single source; no unsupported multi-source join is claimed.
sql_data = df.copy()
for column in sql_data.select_dtypes(include=["category"]).columns:
    sql_data[column] = sql_data[column].astype("string")
with sqlite3.connect(OUTPUT_DIR / "customer_analysis.sqlite") as connection:
    sql_data.to_sql("customers", connection, if_exists="replace", index=False)
    sql_plan_churn = pd.read_sql_query(
        """SELECT plan_type, COUNT(*) AS customers,
                  SUM(churn_flag) AS churned_customers,
                  100.0 * AVG(churn_flag) AS churn_rate_pct,
                  100.0 * (1 - AVG(churn_flag)) AS retention_rate_pct
           FROM customers GROUP BY plan_type ORDER BY churn_rate_pct DESC""",
        connection,
    )
sql_plan_churn.to_csv(OUTPUT_DIR / "plan_churn_sql.csv", index=False)
for name in ["plan_churn", "tenure_churn", "usage_churn", "payment_churn", "support_churn", "login_churn"]:
    globals()[name].rename("churn_rate_pct").to_csv(OUTPUT_DIR / f"{name}.csv")
monthly_retention.to_csv(OUTPUT_DIR / "signup_cohort_retention.csv", index=False)
correlation_matrix.to_csv(OUTPUT_DIR / "correlations.csv")
pd.DataFrame([{
    "total_customers": total_customers,
    "churned_customers": churned_customers,
    "retained_customers": retained_customers,
    "churn_rate_pct": churn_rate,
    "retention_rate_pct": retention_rate,
}]).to_csv(OUTPUT_DIR / "customer_kpis.csv", index=False)
print(f"Analysis saved to {OUTPUT_DIR}")

