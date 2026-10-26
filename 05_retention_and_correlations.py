# Retention trend by signup

monthly_retention = (
    df.groupby(
        "signup_month"
    )["churn_flag"]
    .mean()
    .reset_index()
)


monthly_retention[
    "retention_rate"
] = (
    1 -
    monthly_retention["churn_flag"]
) * 100


print("\nRetention by Signup Month:")

print(
    monthly_retention[
        [
            "signup_month",
            "retention_rate"
        ]
    ]
)


plt.figure(figsize=(12, 6))

sns.lineplot(
    data=monthly_retention,
    x="signup_month",
    y="retention_rate",
    marker="o"
)

plt.title(
    "Retention Rate by Signup Cohort"
)

plt.xlabel(
    "Signup Month"
)

plt.ylabel(
    "Retention Rate (%)"
)

plt.xticks(
    rotation=60
)

plt.tight_layout()

plt.show()


# Correlation matrix

correlation_columns = [
    "monthly_fee",
    "avg_weekly_usage_hours",
    "support_tickets",
    "payment_failures",
    "tenure_months",
    "last_login_days_ago",
    "churn_flag"
]


correlation_matrix = (
    df[correlation_columns]
    .corr()
)


plt.figure(
    figsize=(10, 7)
)

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0
)

plt.title(
    "Correlation Matrix"
)

plt.tight_layout()

plt.show()



