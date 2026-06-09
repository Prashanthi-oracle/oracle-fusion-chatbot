import openpyxl
import pandas as pd

# Read Excel file
df = pd.read_excel("students.xlsx")
print("=== Student Data ===")
print(df)

# Analysis
print("\n=== Analysis ===")
print(f"Total Students: {len(df)}")
print(f"Average Marks: {df['Marks'].mean():.2f}")
print(f"Top Student: {df.loc[df['Marks'].idxmax(), 'Name']}")
print(f"Lowest Score: {df.loc[df['Marks'].idxmin(), 'Name']}")

# Add Pass/Fail column
df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x >= 70 else 'Fail')

# Save back to Excel
df.to_excel("students_result.xlsx", index=False)
print("\n=== Results saved to students_result.xlsx ===")