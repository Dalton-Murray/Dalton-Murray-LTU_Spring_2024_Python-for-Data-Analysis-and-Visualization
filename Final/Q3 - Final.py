#####################
## Dalton Murray    #
## 04/29/2024       #
## Q3               #
#####################
import sys

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Defines the load_data function
def load_data():
    # Loads the customers and orders .csv files into customers and orders dataframes and then returns them
    customers = pd.read_csv("customers.csv")
    orders = pd.read_csv("orders.csv")
    return customers, orders

# Defines the display_data_structure function and takes in customers and orders
def display_data_structure(customers, orders):
    # Print out the head and columns of customers dataframe
    print("First few rows of the Customers DataFrame:")
    print(customers.head())
    print("\nColumn names in Customers DataFrame:")
    print(customers.columns)

    # Print out the head and columns of the orders dataframe
    print("\nFirst few rows of the Orders DataFrame:")
    print(orders.head())
    print("\nColumn names in Orders DataFrame:")
    print(orders.columns)

# Defines the identify_customers_without_orders function and takes in customers and orders
def identify_customers_without_orders(customers, orders):
    # Find all unique customer IDs that have placed an order
    customer_ids_with_orders = orders["customerId"].unique()

    # Use a boolean mask to filter customers who have never placed an order
    customers_without_orders = customers[~customers["id"].isin(customer_ids_with_orders)]

    # Return customers_without_orders
    return customers_without_orders

# Defines the main function
def __main__():
    # Calls the load_data function and sets customers, order dataframes
    customers, orders = load_data()
    # Calls display_data_structure function and passes customers and orders
    display_data_structure(customers, orders)
    # Calls identify_customers_without_orders function and sends customers, orders and sets it to a variable
    customers_without_orders = identify_customers_without_orders(customers, orders)

    # Output the names of customers who have never placed an order
    print("\nCustomers who have never placed an order:")
    print(customers_without_orders[["name"]])

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
