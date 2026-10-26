# 10. OVERALL CHURN / RETENTION RATE

total_customers = len(df)

churned_customers = df["churn_flag"].sum()

retained_customers = (
    total_customers -
    churned_customers
)

churn_rate = (
    churned_customers /
    total_customers
) * 100

retention_rate = (
    retained_customers /
    total_customers
) * 100


print("\n---------------- CUSTOMER KPIs ----------------")

print(
    f"Total Customers: {total_customers:,}"
)

print(
    f"Churned Customers: {churned_customers:,}"
)

print(
    f"Retained Customers: {retained_customers:,}"
)

print(
    f"Churn Rate: {churn_rate:.2f}%"
)

print(
    f"Retention Rate: {retention_rate:.2f}%"
)


# 11. NUMERICAL AND CATEGORICAL COLUMNS

num_cols = [
    "monthly_fee",
    "avg_weekly_usage_hours",
    "support_tickets",
    "payment_failures",
    "tenure_months",
    "last_login_days_ago"
]


cat_cols = [
    "plan_type"
]


print("\nNumerical columns:")
print(num_cols)

print("\nCategorical columns:")
print(cat_cols)


# DISTRIBUTION PLOTS

for col in num_cols:

    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x=col,
        kde=True
    )

    plt.title(
        f"Distribution of {col}"
    )

    plt.xlabel(col)

    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.show()


#KDE PLOTS BY CHURN


kde_cols = [
    "monthly_fee",
    "avg_weekly_usage_hours",
    "tenure_months",
    "last_login_days_ago"
]


for col in kde_cols:

    plt.figure(figsize=(8, 5))

    sns.kdeplot(
        data=df,
        x=col,
        hue="churn",
        fill=True,
        common_norm=False,
        alpha=0.4
    )

    plt.title(
        f"Distribution of {col} by Churn Status"
    )

    plt.xlabel(col)

    plt.ylabel("Density")

    plt.tight_layout()

    plt.show()


#VIOLIN PLOTS BY CHURN

violin_cols = [
    "monthly_fee",
    "avg_weekly_usage_hours",
    "tenure_months",
    "last_login_days_ago"
]


for col in violin_cols:

    plt.figure(figsize=(8, 5))

    sns.violinplot(
        data=df,
        x="churn",
        y=col,
        inner="quartile"
    )

    plt.title(
        f"{col} by Churn Status"
    )

    plt.xlabel("Churn")

    plt.ylabel(col)

    plt.tight_layout()

    plt.show()


