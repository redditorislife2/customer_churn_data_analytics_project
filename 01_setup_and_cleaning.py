# 1. IMPORT LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# 2. DISPLAY SETTINGS
# ----------------------------

sns.set_theme(
    style="whitegrid",
    palette="muted",
    font_scale=1.05
)

pd.set_option("display.max_columns", 200)
pd.set_option("display.width", 120)


# ============================================================
# 3. LOAD DATA
# ============================================================

df = pd.read_csv(
    DATA_PATH
)

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# 4. INITIAL DATA INSPECTION
# ============================================================

print("\n---------------- DATA INFO ----------------")
df.info()

print("\n---------------- DESCRIPTIVE STATISTICS ----------------")
print(df.describe(include="all").T)

print("\n---------------- COLUMN NAMES ----------------")
print(df.columns.tolist())

print("\n---------------- DATA TYPES ----------------")
print(df.dtypes)


# ============================================================
# 5. CHECK MISSING VALUES
# ============================================================

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nTotal missing values:")
print(df.isnull().sum().sum())


# ============================================================
# 6. CHECK DUPLICATES
# ============================================================

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDuplicate user IDs:")
print(df["user_id"].duplicated().sum())


# ============================================================
# 7. DATA CLEANING
# ============================================================

# Remove exact duplicate rows
df = df.drop_duplicates().copy()

# Convert signup_date into datetime
df["signup_date"] = pd.to_datetime(
    df["signup_date"],
    errors="coerce"
)

# Clean categorical text
df["plan_type"] = df["plan_type"].str.strip().str.title()
df["churn"] = df["churn"].str.strip().str.title()


# Convert churn into binary numeric variable
# No = 0
# Yes = 1

df["churn_flag"] = df["churn"].map({
    "No": 0,
    "Yes": 1
})


# Check conversion
print("\nChurn mapping:")
print(
    df[["churn", "churn_flag"]]
    .drop_duplicates()
)


# Validate labels before computing churn and retention rates.
if df.empty:
    raise ValueError("The customer dataset is empty.")
if df["churn_flag"].isna().any():
    raise ValueError("Every churn value must be Yes or No.")
if df["user_id"].isna().any() or df["user_id"].duplicated().any():
    raise ValueError("Expected one row per customer with a nonmissing user_id. Resolve conflicting records first.")

