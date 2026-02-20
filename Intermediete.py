"""
Mini Machine Learning Foundation Project
-----------------------------------------
This script demonstrates:

- File handling (CSV)
- List comprehensions
- Lambda functions
- OOP (Class-based design)
- Importing libraries
- Basic data processing (ML-style)
"""

# ----------------------------------------
# 1️⃣ Importing Libraries
# ----------------------------------------

import csv
import math
import numpy as np
import pandas as pd


# ----------------------------------------
# 2️⃣ Creating a Sample CSV Dataset
# ----------------------------------------

def create_dataset(filename: str) -> None:
    """Creates a sample student dataset."""
    
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Math", "Science", "English"])
        writer.writerow(["Ali", 85, 90, 78])
        writer.writerow(["Sara", 92, 88, 95])
        writer.writerow(["Hamza", 70, 75, 80])


# ----------------------------------------
# 3️⃣ OOP: Data Processor Class
# ----------------------------------------

class DataProcessor:
    """Class to load and process student data."""

    def __init__(self, filename: str):
        self.filename = filename
        self.data = None

    def load_data(self) -> None:
        """Loads CSV data into a pandas DataFrame."""
        self.data = pd.read_csv(self.filename)

    def calculate_average(self) -> None:
        """Adds average column using list comprehension."""
        self.data["Average"] = [
            (row.Math + row.Science + row.English) / 3
            for row in self.data.itertuples()
        ]

    def classify_students(self) -> None:
        """Classifies students using lambda function."""
        self.data["Grade"] = self.data["Average"].apply(
            lambda x: "Pass" if x >= 80 else "Fail"
        )

    def get_top_student(self):
        """Returns student with highest average."""
        return self.data.sort_values(
            by="Average",
            ascending=False
        ).iloc[0]

    def show_data(self) -> None:
        """Displays processed data."""
        print("\nProcessed Dataset:")
        print(self.data)


# ----------------------------------------
# 4️⃣ Main Execution
# ----------------------------------------

if __name__ == "__main__":

    filename = "students.csv"

    # Create dataset
    create_dataset(filename)

    # Initialize processor
    processor = DataProcessor(filename)

    # Load data
    processor.load_data()

    # Process data
    processor.calculate_average()
    processor.classify_students()

    # Display results
    processor.show_data()

    # Show top student
    top_student = processor.get_top_student()
    print("\nTop Student:")
    print(top_student)

    # ----------------------------------------
    # 5️⃣ Using NumPy (ML-style numeric processing)
    # ----------------------------------------

    averages = np.array(processor.data["Average"])
    print("\nMean of averages (NumPy):", np.mean(averages))
    print("Standard deviation:", np.std(averages))