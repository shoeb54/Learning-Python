# ============================================================
# PANDAS MASTER SCRIPT
# Covers: Series, DataFrame, CSV, Cleaning, Missing Values,
# Filtering, Grouping, Feature Selection
# ============================================================

import pandas as pd
import numpy as np


# ============================================================
# 1️⃣ SERIES
# ============================================================

# Series = 1D labeled array
s = pd.Series([10, 20, 30, 40], name="Numbers")
print("Series:\n", s)

# Custom index
s2 = pd.Series([100, 200, 300], index=["a", "b", "c"])
print("\nAccess by label:", s2["b"])


# ============================================================
# 2️⃣ DATAFRAME
# ============================================================

# DataFrame = 2D labeled table
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, np.nan],
    "Salary": [50000, 60000, 55000, 52000],
    "Department": ["HR", "IT", "IT", "HR"]
}

df = pd.DataFrame(data)

print("\nDataFrame:\n", df)
print("\nShape:", df.shape)
print("\nColumns:", df.columns)
print("\nInfo:")
print(df.info())

print("\nSummary Statistics:\n", df.describe())


# ============================================================
# 3️⃣ READING CSV FILE
# ============================================================

# Example (uncomment when using real file)
# df = pd.read_csv("data.csv")

# Common options:
# pd.read_csv("data.csv", sep=",")
# pd.read_csv("data.csv", header=0)


# ============================================================
# 4️⃣ DATA CLEANING
# ============================================================

# Rename column
df.rename(columns={"Salary": "Income"}, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Change data type
df["Age"] = df["Age"].astype("float")

print("\nAfter Cleaning:\n", df)


# ============================================================
# 5️⃣ HANDLING MISSING VALUES
# ============================================================

print("\nMissing Values:\n", df.isnull().sum())

# Drop missing rows
df_dropped = df.dropna()

# Fill missing values
df_filled = df.fillna(df["Age"].mean())

print("\nFilled Missing Values:\n", df_filled)


# ============================================================
# 6️⃣ FILTERING DATA
# ============================================================

# Filter rows
it_employees = df[df["Department"] == "IT"]
print("\nIT Employees:\n", it_employees)

# Multiple conditions
high_income = df[(df["Income"] > 52000) & (df["Department"] == "IT")]
print("\nHigh Income IT:\n", high_income)

# Selecting specific columns
selected_columns = df[["Name", "Income"]]
print("\nSelected Columns:\n", selected_columns)


# ============================================================
# 7️⃣ GROUPING & AGGREGATION
# ============================================================

grouped = df.groupby("Department")["Income"].mean()
print("\nAverage Income by Department:\n", grouped)

# Multiple aggregations
group_multi = df.groupby("Department").agg({
    "Income": ["mean", "max"],
    "Age": "mean"
})
print("\nMultiple Aggregations:\n", group_multi)


# ============================================================
# 8️⃣ FEATURE SELECTION (IMPORTANT FOR ML)
# ============================================================

# Selecting feature columns (X)
X = df[["Age", "Income"]]

# Selecting target column (y)
y = df["Department"]

print("\nFeatures (X):\n", X)
print("\nTarget (y):\n", y)


# Convert categorical column to numerical (Encoding)
df_encoded = pd.get_dummies(df, columns=["Department"])
print("\nEncoded DataFrame:\n", df_encoded)


# ============================================================
# 9️⃣ SORTING & APPLY
# ============================================================

# Sorting
df_sorted = df.sort_values(by="Income", ascending=False)
print("\nSorted by Income:\n", df_sorted)

# Apply custom function
df["Income_in_Thousands"] = df["Income"].apply(lambda x: x / 1000)
print("\nApplied Function:\n", df)


# ============================================================
# END
# ============================================================