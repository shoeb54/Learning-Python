# ============================================================
# FULL EDA WORKFLOW SCRIPT
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# ------------------------------------------------------------
# 1️⃣ LOAD DATA
# ------------------------------------------------------------

# Replace with your dataset
# df = pd.read_csv("your_dataset.csv")

# Sample synthetic dataset for demonstration
df = pd.DataFrame({
    "Age": np.random.randint(18, 60, 200),
    "Salary": np.random.randint(20000, 100000, 200),
    "Experience": np.random.randint(1, 20, 200),
    "Department": np.random.choice(["HR", "IT", "Sales"], 200),
    "Target": np.random.choice([0, 1], 200)
})

print("First 5 rows:")
print(df.head())

# ------------------------------------------------------------
# 2️⃣ BASIC DATA INSPECTION
# ------------------------------------------------------------

print("\nShape:", df.shape)
print("\nColumns:", df.columns)
print("\nData Types:")
print(df.dtypes)

print("\nInfo:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())


# ------------------------------------------------------------
# 3️⃣ CHECK MISSING VALUES
# ------------------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# Example handling missing values (if any)
df.fillna(df.mean(numeric_only=True), inplace=True)


# ------------------------------------------------------------
# 4️⃣ UNIVARIATE ANALYSIS (Single Variable)
# ------------------------------------------------------------

# Histogram
plt.figure()
sns.histplot(df["Salary"], bins=30, kde=True)
plt.title("Salary Distribution")
plt.show()

# Countplot (Categorical)
plt.figure()
sns.countplot(x="Department", data=df)
plt.title("Department Distribution")
plt.show()


# ------------------------------------------------------------
# 5️⃣ BIVARIATE ANALYSIS (Two Variables)
# ------------------------------------------------------------

# Scatter Plot
plt.figure()
sns.scatterplot(x="Experience", y="Salary", hue="Department", data=df)
plt.title("Experience vs Salary")
plt.show()

# Boxplot
plt.figure()
sns.boxplot(x="Department", y="Salary", data=df)
plt.title("Salary by Department")
plt.show()


# ------------------------------------------------------------
# 6️⃣ CORRELATION ANALYSIS
# ------------------------------------------------------------

corr = df.corr(numeric_only=True)

plt.figure()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# ------------------------------------------------------------
# 7️⃣ OUTLIER DETECTION
# ------------------------------------------------------------

plt.figure()
sns.boxplot(y=df["Salary"])
plt.title("Salary Outliers")
plt.show()

# Removing outliers using IQR method
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

df = df[(df["Salary"] >= Q1 - 1.5*IQR) & 
        (df["Salary"] <= Q3 + 1.5*IQR)]


# ------------------------------------------------------------
# 8️⃣ FEATURE ENGINEERING
# ------------------------------------------------------------

# Create new feature
df["Salary_per_Experience"] = df["Salary"] / df["Experience"]

# Encode categorical variables
df = pd.get_dummies(df, columns=["Department"], drop_first=True)


# ------------------------------------------------------------
# 9️⃣ FEATURE SELECTION
# ------------------------------------------------------------

X = df.drop("Target", axis=1)
y = df["Target"]

print("\nFinal Feature Set:")
print(X.head())

print("\nTarget Variable:")
print(y.head())


# ------------------------------------------------------------
# 🔟 SAVE CLEANED DATASET
# ------------------------------------------------------------

# df.to_csv("cleaned_data.csv", index=False)

print("\nEDA Completed Successfully")