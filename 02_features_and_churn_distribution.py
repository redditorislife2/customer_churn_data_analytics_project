#  Features

# Extract signup year and month

df["signup_year"] = df["signup_date"].dt.year

df["signup_month"] = (
    df["signup_date"]
    .dt.to_period("M")
    .astype(str)
)


# Create tenure groups

df["tenure_group"] = pd.cut(
    df["tenure_months"],
    bins=[
        -1,
        6,
        12,
        24,
        36,
        np.inf
    ],
    labels=[
        "0-6 Months",
        "7-12 Months",
        "13-24 Months",
        "25-36 Months",
        "37+ Months"
    ]
)


# Create usage groups

df["usage_group"] = pd.cut(
    df["avg_weekly_usage_hours"],
    bins=[
        -1,
        5,
        10,
        20,
        np.inf
    ],
    labels=[
        "Very Low",
        "Low",
        "Medium",
        "High"
    ]
)


# Create login activity groups

df["login_activity"] = pd.cut(
    df["last_login_days_ago"],
    bins=[
        -1,
        7,
        14,
        30,
        np.inf
    ],
    labels=[
        "Active",
        "Moderately Active",
        "Inactive",
        "Very Inactive"
    ]
)


# Binary indicator for payment failures

df["has_payment_failure"] = (
    df["payment_failures"] > 0
).astype(int)


# Binary indicator for support tickets

df["has_support_ticket"] = (
    df["support_tickets"] > 0
).astype(int)


# Target variable distribution

print("\nTarget Variable Counts:")

print(
    df["churn"]
    .value_counts()
)


print("\nTarget Variable Percentages:")

print(
    df["churn"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)


# Plot churn distribution

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="churn"
)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.show()




