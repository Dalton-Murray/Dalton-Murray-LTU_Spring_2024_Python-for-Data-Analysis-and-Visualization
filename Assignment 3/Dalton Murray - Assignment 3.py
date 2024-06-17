#####################
## Dalton Murray    #
## 03/28/2024       #
## Assingment 3     #
#####################
import sys
import os

import pandas as pd # Import the pandas library and sets an alias to pa
import numpy as np # Import the numpy library and sets an alias to np
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt
import seaborn as sns # Imports seaborn library and sets an alias to sns

# Defines the __main__ function
def __main__():
    ## Task 0 - Load datasets
    sales_data = pd.read_csv("./Sales_Data.csv")
    customer_data = pd.read_csv("./Customer_Data.csv")

    ## Task 1 - Data Exploration and Cleaning
    # Basic statistics - Mean, Median, Standard Deviation
    sales_statistics = sales_data.describe().loc[["mean", "std", "50%"]].rename(index={"50%": "median"})
    customer_statistics = customer_data.describe().loc[["mean", "std", "50%"]].rename(index={"50%": "median"})
    print("The basic statistics for sales data is:\n", sales_statistics)
    print("\nThe basic statistics for customer data is:\n", customer_statistics)

    # Missing values in customer data
    # Since it wasn"t specific what to replace the missing values with, I just replaced it with "NA"
    customer_data.fillna("NA", inplace = True)
    print("\nCustomer data:\n", customer_data.head(5))

    # Convert Date column to datetime format and extract the year and month into separate columns
    sales_data["Date"] = pd.to_datetime(sales_data["Date"])
    sales_data["Year"] = sales_data["Date"].dt.year
    sales_data["Month"] = sales_data["Date"].dt.month
    print("\nSales data:\n", sales_data.head(5))

    customer_data["Date"] = pd.to_datetime(sales_data["Date"])
    customer_data["Year"] = customer_data["Date"].dt.year
    customer_data["Month"] = customer_data["Date"].dt.month
    print("\nCustomer data:\n", customer_data.head(5))

    ## Task 2 - Data Merging and Joining
    # Merge the Sales Data and Customer Data on Customer_ID
    merged_data = pd.merge(customer_data, sales_data, on = "Customer_ID", how = "left")
    print("\nMerged Data:\n", merged_data.head(5))

    # Identify customers without purchases
    customersNoPurchases = merged_data[merged_data["Transaction_ID"].isnull()]
    print("\nCustomers without purchases:\n", customersNoPurchases.head(5))

    ## Task 3 - Aggregation and grouping
    # Total units sold and total sales
    productCategoryTotals = merged_data.groupby("Product_Category").agg({"Unit_Sold": "sum", "Total_Sales": "sum"})
    print("\nTotal units sold and total sales for each product category:\n", productCategoryTotals)

    # Calculate total sales per customer
    customer_sales = merged_data.groupby("Customer_ID")["Total_Sales"].sum()
    print("Average purchase amount per customer:\n", customer_sales.head(5))

    # Calculate quantiles based on total sales per customer
    quantiles = customer_sales.quantile([0.25, 0.5, 0.75])

    # Categorize customers as "High spender", "Medium spender", and "Low spender" based on quantiles
    customerQuantiles = customer_sales.apply(
        lambda x: "High spender"
        if x >= quantiles[0.75]
        else ("Medium spender"
            if x >= quantiles[0.5]
            else "Low spender")
    )

    print("\nCustomer quantiles:\n", customerQuantiles.head(5))

    ## Task 4 - Time series analysis
    # Analyze sales trends over months
    monthly_sales = merged_data.groupby("Month")["Total_Sales"].sum()
    plt.figure(figsize = (10, 6))
    monthly_sales.plot(kind="line", marker = "o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.grid(True)
    plt.xticks(range(1, 13))
    # plt.show()

    # Identify the month with the highest sales
    monthHighestSale = monthly_sales.idxmax()
    highestSalesAmount = monthly_sales.max()
    print("\nThe month with the highest sales is:", monthHighestSale)
    print("\nThis month has a total sales of: $", highestSalesAmount)

    # Month-Over-Month growth rate in sales
    monthlyGrowthRate = monthly_sales.pct_change() * 100
    print("\nMonth-over-month growth rate in sales:\n", monthlyGrowthRate)

    ## Task 5 - Customer Demographics Analysis
    # Age distribution of customers
    plt.figure(figsize = (10, 6))
    sns.histplot(customer_data["Age"], bins = 20, kde = True)
    plt.title("Age Distribution of Customers")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.grid(True)
    # plt.show()

    # Most prevalent age group
    mostPrevalentAgeGroup = customer_data["Age"].mode()[0]
    print("\nThe most prevalent age group is:", mostPrevalentAgeGroup)

    # Membership tier distribution
    plt.figure(figsize = (8, 5))
    sns.countplot(x = "Membership_Tier", data = merged_data, palette = "Set2", hue = "Membership_Tier")
    plt.title("Membership Tier Distribution")
    plt.xlabel("Membership Tier")
    plt.ylabel("Count")
    plt.grid(axis = "y")
    # plt.show()

    # Calculate total sales for each membership tier
    membershipSales = merged_data.groupby("Membership_Tier")["Total_Sales"].sum()
    print("\nTotal sales for each membership tier:\n", membershipSales)

    # Analyze the correlation between membership tiers and sales
    correlation = merged_data.groupby("Membership_Tier")["Total_Sales"].mean()
    print("\nCorrelation between membership tiers and average sales:\n", correlation)

    ## Task 6 - Regional analysis
    # Total sales and average unit price in each region
    region_data = merged_data.groupby("Region")
    regionAvgPrice = region_data.agg({"Total_Sales": "sum", "Price_per_Unit": "mean"})

    print("Total sales and average unit price in each region:\n", regionAvgPrice)

    # Product category highest sales
    regionHighestSalesCat = region_data.apply(lambda x: x.groupby("Product_Category")["Total_Sales"].sum().idxmax())

    print("\nProduct category with the highest sales in each region:\n", regionHighestSalesCat)

    ## Task 7 - Advanced analysis
    # Top 10 customers purchase amount
    topCustomers = merged_data.groupby("Customer_ID")["Total_Sales"].sum().nlargest(10)
    print("\nTop 10 customers based on purchase amount:\n", topCustomers)

    # Analyze buying pattern
    topCustomers_data = merged_data[merged_data["Customer_ID"].isin(topCustomers.index)]
    print("\nBuying patterns of top customers:\n", topCustomers_data.head(5))

    # Pivot table showing total units sold per prduct category across each region
    pivotTableTopCustomer = pd.pivot_table(topCustomers_data, values = "Unit_Sold", index = "Product_Category", columns = "Region", aggfunc = "sum", fill_value = 0)
    print("\nPivot table showing total units sold for each product category across each region:\n", pivotTableTopCustomer)

    ## Task 8 - Visualization
    # Bar chart showing number of transactions per product category
    transactionCount = merged_data["Product_Category"].value_counts()
    plt.figure(figsize=(10, 6))
    transactionCount.plot(kind = "bar")
    plt.title("Number of Transactions per Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Number of Transactions")
    plt.xticks(rotation = 45, ha = "right")
    plt.tight_layout()
    # plt.show()

    # Line graph of monthly sales over year
    monthlySales = merged_data.groupby("Month")["Total_Sales"].sum()
    plt.figure(figsize = (10, 6))
    monthly_sales.plot(marker = "o", linestyle = "-")
    plt.title("Monthly Sales Over the Year")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(monthly_sales.index)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
