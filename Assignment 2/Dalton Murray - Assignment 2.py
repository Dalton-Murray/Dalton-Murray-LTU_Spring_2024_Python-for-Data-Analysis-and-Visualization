#####################
## Dalton Murray    #
## 02/12/2024       #
## Assingment 2     #
#####################
import sys
import os

import pandas as pd # Import the pandas library and sets an alias to pa
import numpy as np
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt

# Defines the __main__ function
def __main__():

    ## Task 1
    # Sets the database location to the relative folder
    database = "./"
    # Sets the salesQ1 and salesQ2 variables to dataframes of the read csv's
    salesQ1 = pd.read_csv(os.path.join(database, "./sales_q1-1.csv"))
    salesQ2 = pd.read_csv(os.path.join(database, "./sales_q2-1.csv"))
    # Prints the first 5 rows of the dataframes
    print("Sales Q1:\n", salesQ1.head(5))
    print("Sales Q2:\n", salesQ2.head(5))
    # Checks for missing values in the dataframes by checking if a value is null
    # Then summarizing/printing out the list of null values
    print("Sales Q1 missing summary:\n", salesQ1.isnull().sum())
    print("Sales Q2 missing summary:\n", salesQ2.isnull().sum())

    ## Task 2
    # Adds a total sales column by multiplying the existing price by quantity for each dataframe
    salesQ1["Total_Sales"] = salesQ1["Price"] * salesQ1["Quantity"]
    salesQ2["Total_Sales"] = salesQ2["Price"] * salesQ2["Quantity"]
    # Creates a series from the first data frame's product id column
    salesQ1Series = salesQ1["Product_ID"]
    # Print out information about the series
    print("Sales Q1 product ID head:\n",salesQ1Series.head())
    print("Sales Q1 product ID tail:\n", salesQ1Series.tail())
    print("Sales Q1 product ID describe:\n", salesQ1Series.describe())

    ## Task 3
    # Concatenate salesQ1 and salesQ2 into combined_sales along the axis 0 and ignore its index
    combined_sales = pd.concat([salesQ1, salesQ2], axis = 0, ignore_index=True)
    print("Combined quarters:\n", combined_sales.head())

    ## Task 4
    # Groups the Product_ID's and then sorts it by the total sales in descending order
    productGroupBy = combined_sales.groupby("Product_ID")["Total_Sales"].sum()
    productSort = productGroupBy.sort_values(ascending = False)
    print("Grouped & sorted products:\n", productSort)

    ## Task 5
    # Filters out/removes the rows where quantity is greater than 50
    quantityFilter = combined_sales[combined_sales["Quantity"] < 50]
    print("Filtered quantity:\n", quantityFilter)

    ## Task 6
    # If there is a missing value in either price or quantity it will fill it in inplace (without returning a new dataframe)
    # with the mean or average of their respective column price or quantity
    combined_sales["Price"].fillna(combined_sales["Price"].mean(), inplace = True)
    combined_sales["Quantity"].fillna(combined_sales["Quantity"].mean(), inplace = True)

    ## Task 7
    # Saves a csv file of the analysis performed
    combined_sales.to_csv("combined_sales_analysis.csv", index = False)

    ## Task 8
    top5Products = productSort.head(5)
    plt.bar(top5Products.index, top5Products.values)
    plt.xlabel("Product ID")
    plt.ylabel("Total Sales in USD")
    plt.title("Top 5 Products")
    plt.show()

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
