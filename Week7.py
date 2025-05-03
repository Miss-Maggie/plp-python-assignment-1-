# Task 1: Load and Explore the Dataset
import pandas as pd 
data = pd.read_csv('student_data.csv')
print(data)

df = pd.read_csv('student_data.csv')
print(df.head()) 
print(df.info())        
print(df.isnull().sum())

# Task 2: Basic Data Analysis
df = pd.read_csv('student_data.csv')
# 1. Display basic statistics for numerical columns
print("📊 Basic Statistics:\n")
print(df.describe())

# 2. Group by 'Subject' and compute average Score and Attendance
print("\n📚 Average Score and Attendance by Subject:\n")
print(df.groupby('Subject')[['Score', 'Attendance %']].mean().reset_index())

# Task 3: Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Line Chart: Score Trend Across Students (simulating time with StudentID)
plt.figure(figsize=(8, 4))
sns.lineplot(x='StudentID', y='Score', data=df, marker='o')
plt.title("📈 Score Trend Across Students")
plt.xlabel("StudentID")
plt.ylabel("Score")
plt.tight_layout()
plt.show()

# 2. Bar Chart: Average Score by Subject
plt.figure(figsize=(8, 4))
sns.barplot(x='Subject', y='Score', data=df, ci=None)
plt.title("📊 Average Score per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of Attendance
plt.figure(figsize=(8, 4))
sns.histplot(df['Attendance %'], bins=5, kde=True)
plt.title("📉 Distribution of Attendance %")
plt.xlabel("Attendance %")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Score vs. Attendance
plt.figure(figsize=(8, 4))
sns.scatterplot(x='Attendance %', y='Score', hue='Gender', style='Subject', data=df)
plt.title("🔍 Score vs. Attendance by Gender and Subject")
plt.xlabel("Attendance %")
plt.ylabel("Score")
plt.tight_layout()
plt.show()


# Error handling and data cleaning
import pandas as pd

try:
    # Try to load the CSV file
    df = pd.read_csv("student_scores.csv")

    # Display first few rows
    print("✅ Data loaded successfully:")
    print(df.head())

    # Clean column names (remove spaces)
    df.columns = df.columns.str.replace(' ', '')

    # Check for missing values
    if df.isnull().values.any():
        print("\n⚠️ Missing values found. Filling with 0...")
        df = df.fillna(0)  # You can also use dropna() if preferred

    # Convert Score column to numeric (in case of invalid entries)
    df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
    if df['Score'].isnull().any():
        print("⚠️ Invalid scores found and set to NaN. Filling with average score.")
        df['Score'].fillna(df['Score'].mean(), inplace=True)

    print("\n✅ Cleaned Data:")
    print(df.info())

except FileNotFoundError:
    print("❌ Error: The file 'student_scores.csv' was not found.")
except pd.errors.ParserError:
    print("❌ Error: Could not parse the CSV file. Check formatting.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")