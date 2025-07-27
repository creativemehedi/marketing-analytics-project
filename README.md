# Marketing and Sales Performance Analysis

## Project Overview

This project focuses on analyzing the impact of different marketing channels (TV, Radio, Social Media) and influencer types on sales. It aims to identify key trends, understand the relationships between marketing spend and sales, and provide insights for optimizing marketing campaigns. The analysis utilizes a dummy dataset to demonstrate data cleaning, exploratory data analysis (EDA), and basic predictive modeling techniques.

## Dataset

The dataset used in this project is `DummyDataHSS.csv`. It contains the following columns:

*   `TV`: TV promotion budget (in million)
*   `Radio`: Radio promotion budget (in million)
*   `Social Media`: Social Media promotion budget (in million)
*   `Influencer`: Type of influencer (Mega, Macro, Nano, Micro)
*   `Sales`: Sales (in million)

## Methodology

The project follows a standard data analysis workflow:

1.  **Data Loading and Initial Exploration:** The dataset is loaded using Python's pandas library. Initial checks are performed to understand the data structure, identify missing values, and get a statistical summary.
2.  **Data Cleaning and Preparation:** Missing values in numerical columns (`TV`, `Radio`, `Social Media`, `Sales`) are imputed using their respective medians. This ensures data integrity for subsequent analysis.
3.  **Exploratory Data Analysis (EDA):**
    *   **Correlation Analysis:** A heatmap visualizes the correlation matrix between marketing spends and sales, highlighting the strength and direction of relationships.
    *   **Distribution Analysis:** Histograms show the distribution of marketing budgets and sales.
    *   **Influencer Impact Analysis:** Box plots illustrate the sales performance across different influencer types, helping to identify which categories are most effective.
4.  **Basic Predictive Modeling:** A simple linear regression model is built to predict sales based on the marketing budgets. The model's performance is evaluated using Mean Squared Error (MSE) and R-squared (R2) metrics, and a plot of actual vs. predicted sales is generated.

## Tools and Technologies

*   **Python:** For data manipulation, analysis, and visualization.
    *   `pandas`: Data structures and analysis tools.
    *   `numpy`: Numerical operations.
    *   `matplotlib` & `seaborn`: Data visualization.
    *   `scikit-learn`: Machine learning (Linear Regression).
*   **SQL Concepts:** Discussed for conceptual understanding of data cleaning and preparation in a database environment.
*   **Power BI / Tableau (Conceptual):** A dashboard mockup is provided to illustrate how the insights could be presented interactively.

## Project Structure
marketing-analytics-project/
├── DummyDataHSS.csv
├── marketing_analysis.py
├── correlation_matrix.png
├── distributions.png
├── sales_by_influencer.png
├── actual_vs_predicted_sales.png
├── dashboard_mockup.md
└── README.md
