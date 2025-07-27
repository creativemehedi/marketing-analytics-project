
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def load_and_explore_data(file_path):
    """
    Loads the dataset and performs initial data exploration.
    """
    print(f"\n--- Loading data from: {file_path} ---")
    df = pd.read_csv(file_path)

    print("\n--- Dataset Head ---")
    print(df.head())

    print("\n--- Dataset Info ---")
    df.info()

    print("\n--- Dataset Description ---")
    print(df.describe())

    print("\n--- Missing Values Before Cleaning ---")
    print(df.isnull().sum())

    return df

def clean_data(df):
    """
    Handles missing values in the dataset.
    For numerical columns, missing values will be filled with the median.
    """
    print("\n--- Cleaning Data ---")
    for col in ['TV', 'Radio', 'Social Media', 'Sales']:
        if df[col].isnull().any():
            median_val = df[col].median()
            df[col].fillna(median_val, inplace=True)
            print(f"Filled missing values in {col} with median: {median_val}")

    print("\n--- Missing Values After Cleaning ---")
    print(df.isnull().sum())
    return df

def perform_eda(df):
    """
    Performs Exploratory Data Analysis (EDA).
    """
    print("\n--- Performing Exploratory Data Analysis (EDA) ---")

    # Correlation Analysis
    print("\n--- Correlation Matrix ---")
    correlation_matrix = df[['TV', 'Radio', 'Social Media', 'Sales']].corr()
    print(correlation_matrix)

    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix of Marketing Spend and Sales')
    plt.savefig('correlation_matrix.png')
    plt.close()
    print("Saved correlation_matrix.png")

    # Distribution Analysis
    print("\n--- Distribution of Sales and Marketing Budgets ---")
    df[['TV', 'Radio', 'Social Media', 'Sales']].hist(bins=15, figsize=(12, 8))
    plt.suptitle('Distribution of Marketing Budgets and Sales')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('distributions.png')
    plt.close()
    print("Saved distributions.png")

    # Influencer Impact Analysis
    print("\n--- Sales by Influencer Type ---")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Influencer', y='Sales', data=df)
    plt.title('Sales Performance by Influencer Type')
    plt.xlabel('Influencer Type')
    plt.ylabel('Sales (in million)')
    plt.savefig('sales_by_influencer.png')
    plt.close()
    print("Saved sales_by_influencer.png")

    print("EDA complete. Check the generated PNG files for visualizations.")

def perform_predictive_modeling(df):
    """
    Performs basic predictive modeling using Linear Regression.
    """
    print("\n--- Performing Predictive Modeling (Linear Regression) ---")

    # Prepare data for modeling
    X = df[['TV', 'Radio', 'Social Media']]
    y = df['Sales']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"R-squared (R2): {r2:.2f}")

    # Plotting actual vs. predicted sales
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.6)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
    plt.xlabel('Actual Sales')
    plt.ylabel('Predicted Sales')
    plt.title('Actual vs. Predicted Sales')
    plt.savefig('actual_vs_predicted_sales.png')
    plt.close()
    print("Saved actual_vs_predicted_sales.png")

    print("Predictive modeling complete.")

if __name__ == "__main__":
    file_path = "DummyDataHSS.csv"
    df = load_and_explore_data(file_path)
    df_cleaned = clean_data(df)
    perform_eda(df_cleaned)
    perform_predictive_modeling(df_cleaned)

    print("\n--- SQL Concepts for Data Cleaning/Preparation ---")
    print("In SQL, similar data cleaning steps would involve:")
    print("1. Identifying missing values: `SELECT COUNT(*) FROM your_table WHERE column_name IS NULL;`")
    print("2. Filling missing numerical values (e.g., with median/average):")
    print("   `UPDATE your_table SET column_name = (SELECT MEDIAN(column_name) FROM your_table) WHERE column_name IS NULL;`")
    print("3. Filtering out rows with missing values: `SELECT * FROM your_table WHERE column_name IS NOT NULL;`")
    print("4. Correcting/Categorizing data: `UPDATE your_table SET column_name = 'NewCategory' WHERE column_name = 'OldCategory';` or `CASE WHEN ... THEN ... END` statements.")
    print("5. Removing duplicates: `DELETE FROM your_table WHERE rowid NOT IN (SELECT MIN(rowid) FROM your_table GROUP BY column1, column2, ...);`")


