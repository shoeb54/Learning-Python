# ============================================================
# MATPLOTLIB MASTER SCRIPT
# Covers: Line, Bar, Histogram, Heatmap
# ============================================================

import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------
# 1️⃣ BASIC LINE PLOT
# ------------------------------------------------------------

x = np.arange(0, 10)
y = x ** 2

plt.figure()
plt.plot(x, y)
plt.title("Line Plot: y = x^2")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()


# ------------------------------------------------------------
# 2️⃣ MULTIPLE LINE PLOTS
# ------------------------------------------------------------

y2 = x ** 3

plt.figure()
plt.plot(x, y, label="x^2")
plt.plot(x, y2, label="x^3")
plt.legend()
plt.title("Multiple Lines")
plt.show()


# ------------------------------------------------------------
# 3️⃣ BAR CHART
# ------------------------------------------------------------

categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]

plt.figure()
plt.bar(categories, values)
plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()


# ------------------------------------------------------------
# 4️⃣ HISTOGRAM
# ------------------------------------------------------------

data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# ------------------------------------------------------------
# 5️⃣ CORRELATION HEATMAP (MANUAL WITH MATPLOTLIB)
# ------------------------------------------------------------

# Create random dataset
data_matrix = np.random.rand(5, 5)

# Correlation matrix
corr = np.corrcoef(data_matrix)

plt.figure()
plt.imshow(corr)
plt.colorbar()
plt.title("Correlation Heatmap (Matplotlib)")
plt.xticks(range(5))
plt.yticks(range(5))
plt.show()