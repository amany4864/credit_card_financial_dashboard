# Credit Card Financial Dashboard

This project provides a comprehensive analysis of credit card customer and transaction data. It includes a Power BI dashboard for visualizing key metrics, a detailed exploratory data analysis (EDA) in a Jupyter Notebook, and a Python script for ingesting the data into a MySQL database.

## Features

*   **Interactive Power BI Dashboard:** A user-friendly dashboard to visualize and explore the financial data.
*   **In-depth Exploratory Data Analysis (EDA):** A Jupyter Notebook that provides a deep dive into the customer and transaction data, uncovering insights and trends.
*   **Automated Data Ingestion:** A Python script that continuously checks for new data and ingests it into a MySQL database.
*   **Detailed PDF Reports:** Two PDF reports summarizing the findings from the customer and transaction data.

## Data Sources

The project uses two CSV files as the primary data sources:

*   `cc_customer.csv`: Contains information about the credit card customers, such as age, gender, marital status, income, etc.
*   `cc_transaction.csv`: Contains information about the credit card transactions, such as card category, annual fees, credit limit, total transaction amount, etc.

## Exploratory Data Analysis (EDA)

The `cc_financial_dashboard_EDA.ipynb` Jupyter Notebook performs a detailed EDA on the provided datasets. The key steps in the EDA include:

*   **Data Loading and Cleaning:** Loading the CSV files into Pandas DataFrames and checking for missing values.
*   **Data Merging:** Merging the customer and transaction dataframes to create a unified dataset.
*   **Feature Engineering:** Creating new features like `Revenue`, `AgeGroup`, and `Income_Group` to facilitate analysis.
*   **Data Visualization:** Creating various plots and charts to visualize the data and uncover insights.
*   **Correlation Analysis:** Analyzing the correlation between different numerical features.

### Key Insights from the EDA:

*   The top 10 spenders are high-income customers.
*   The 50-60 age group contributes the most revenue.
*   High-income females are the most profitable group in the high-income segment.
*   Revenue is strongly correlated with interest earned.
*   Total transaction amount and total transaction volume are highly correlated.

## Database Schema

The `ingestion_mysql.py` script ingests the data into a MySQL database with the following tables:

*   **customer:** Stores the customer data from `cc_customer.csv`.
*   **transaction:** Stores the transaction data from `cc_transaction.csv`.

The script uses the `Client_Num` column as the primary key to join the two tables.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/aman4864y/credit_card_financial_dashboard.git
    ```
2.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up the MySQL database:**
    *   Create a MySQL database.
    *   Create a `.env` file in the root directory of the project and add the following environment variables:
        ```
        MYSQL_HOST=your_mysql_host
        MYSQL_PORT=your_mysql_port
        MYSQL_USER=your_mysql_user
        MYSQL_PASSWORD=your_mysql_password
        MYSQL_DB=your_mysql_database
        ```

## Usage

### Data Ingestion

The `ingestion_mysql.py` script is used to ingest the data into the MySQL database. The script continuously checks for new CSV files in the `data` directory and ingests them into the corresponding tables.

To run the script:

```bash
python ingestion_mysql.py
```

### Power BI Dashboard

The Power BI dashboard can be opened using the `credit card customer dashboard.pbix` file. The dashboard is connected to the MySQL database and provides an interactive way to visualize the data.

## Reports

The project includes two PDF reports:

*   `credit card customer dashboard.pdf`: A PDF version of the Power BI dashboard.
*   `credit card transaction report.pdf`: A detailed report on the credit card transaction data.

## Future Work

*   **Predictive Modeling:** Build a machine learning model to predict customer churn or fraudulent transactions.
*   **Real-time Dashboard:** Create a real-time dashboard using a streaming data pipeline.
*   **More Data Sources:** Integrate more data sources, such as social media data, to get a more holistic view of the customers.
