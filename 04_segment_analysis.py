# CHURN BY PLAN TYPE

plan_churn = (
    df.groupby(
        "plan_type",
        observed=True
    )["churn_flag"]
    .mean()
    .mul(100)
    .sort_values(
        ascending=False
    )
)


print("\nChurn Rate by Plan Type:")

print(plan_churn)


plt.figure(figsize=(8, 5))

sns.barplot(
    x=plan_churn.index,
    y=plan_churn.values
)

plt.title(
    "Churn Rate by Plan Type"
)

plt.xlabel(
    "Plan Type"
)

plt.ylabel(
    "Churn Rate (%)"
)

plt.tight_layout()

plt.show()


#CHURN BY TENURE GROUP

tenure_churn = (
    df.groupby(
        "tenure_group",
        observed=True
    )["churn_flag"]
    .mean()
    .mul(100)
)


print("\nChurn Rate by Tenure Group:")

print(tenure_churn)


plt.figure(figsize=(9, 5))

sns.barplot(
    x=tenure_churn.index,
    y=tenure_churn.values
)

plt.title(
    "Churn Rate by Customer Tenure"
)

plt.xlabel(
    "Tenure Group"
)

plt.ylabel(
    "Churn Rate (%)"
)

plt.xticks(
    rotation=25
)

plt.tight_layout()

plt.show()


# CHURN BY USAGE GROUP

usage_churn = (
    df.groupby(
        "usage_group",
        observed=True
    )["churn_flag"]
    .mean()
    .mul(100)
)


print("\nChurn Rate by Usage Group:")

print(usage_churn)


plt.figure(figsize=(8, 5))

sns.barplot(
    x=usage_churn.index,
    y=usage_churn.values
)

plt.title(
    "Churn Rate by Weekly Usage"
)

plt.xlabel(
    "Usage Group"
)

plt.ylabel(
    "Churn Rate (%)"
)

plt.tight_layout()

plt.show()


# PAYMENT FAILURES VS CHURN

payment_churn = (
    df.groupby(
        "payment_failures"
    )["churn_flag"]
    .mean()
    .mul(100)
)


print("\nChurn Rate by Payment Failures:")

print(payment_churn)


plt.figure(figsize=(8, 5))

sns.barplot(
    x=payment_churn.index,
    y=payment_churn.values
)

plt.title(
    "Churn Rate by Number of Payment Failures"
)

plt.xlabel(
    "Payment Failures"
)

plt.ylabel(
    "Churn Rate (%)"
)

plt.tight_layout()

plt.show()


# SUPPORT TICKETS VS CHURN

support_churn = (
    df.groupby(
        "support_tickets"
    )["churn_flag"]
    .mean()
    .mul(100)
)


print("\nChurn Rate by Support Tickets:")

print(support_churn)


plt.figure(figsize=(9, 5))

sns.barplot(
    x=support_churn.index,
    y=support_churn.values
)

plt.title(
    "Churn Rate by Support Tickets"
)

plt.xlabel(
    "Support Tickets"
)

plt.ylabel(
    "Churn Rate (%)"
)

plt.tight_layout()

plt.show()


# LAST LOGIN ACTIVITY VS CHURN

login_churn = (
    df.groupby(
        "login_activity",
        observed=True
    )["churn_flag"]
    .mean()
    .mul(100)
)


print("\nChurn Rate by Login Activity:")

print(login_churn)


plt.figure(figsize=(9, 5))

sns.barplot(
    x=login_churn.index,
    y=login_churn.values
)

plt.title(
    "Churn Rate by Login Activity"
)

plt.xlabel(
    "Login Activity"
)

plt.ylabel(
    "Churn Rate (%)"
)

plt.xticks(
    rotation=20
)

plt.tight_layout()

plt.show()


