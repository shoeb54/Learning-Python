# ============================================================
# SEABORN MASTER SCRIPT
# Covers: Line, Bar, Histogram, Correlation Heatmap
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set style
sns.set_theme(style="whitegrid")

# Sample dataset
df = pd.DataFrame({
    "x": np.arange(0, 10),
    "y1": np.arange(0, 10) ** 2,
    "y2": np.arange(0, 10) ** 3
})


# ------------------------------------------------------------
# 1️⃣ LINE PLOT
# ------------------------------------------------------------

plt.figure()
sns.lineplot(x="x", y="y1", data=df)
plt.title("Line Plot (Seaborn)")
plt.show()


# ------------------------------------------------------------
# 2️⃣ MULTIPLE LINE PLOTS
# ------------------------------------------------------------

plt.figure()
sns.lineplot(x="x", y="y1", data=df, label="x^2")
sns.lineplot(x="x", y="y2", data=df, label="x^3")
plt.title("Multiple Lines")
plt.show()


# ------------------------------------------------------------
# 3️⃣ BAR CHART
# ------------------------------------------------------------

categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]

bar_df = pd.DataFrame({"Category": categories, "Value": values})

plt.figure()
sns.barplot(x="Category", y="Value", data=bar_df)
plt.title("Bar Chart (Seaborn)")
plt.show()


# ------------------------------------------------------------
# 4️⃣ HISTOGRAM
# ------------------------------------------------------------

data = np.random.randn(1000)

plt.figure()
sns.histplot(data, bins=30, kde=True)
plt.title("Histogram (Seaborn)")
plt.show()


# ------------------------------------------------------------
# 5️⃣ CORRELATION HEATMAP
# ------------------------------------------------------------

# Create DataFrame
data_matrix = pd.DataFrame(np.random.rand(5, 5), 
                           columns=["A", "B", "C", "D", "E"])

corr = data_matrix.corr()

plt.figure()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (Seaborn)")
plt.show()