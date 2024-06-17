#####################
## Dalton Murray    #
## 04/29/2024       #
## Q2               #
#####################
import sys

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Defines the load_data function
def load_data():
    # Load the world_data.csv file as a dataframe called data
    data = pd.read_csv("world_data.csv")
    # Returns the data dataframe
    return data

# Defines the display_data_structure function and takes in the data dataframe
def display_data_structure(data):
    print("First few rows of the dataset:")
    # Print out the head of the data dataframe
    print(data.head())
    print("\nColumn names:")
    # Print out the columns of the data dataframe
    print(data.columns)

# Defines the identify_big_countries function and takes in the data dataframe
def identify_big_countries(data):
    # Define "big" country criteria
    area_criteria = 3000000
    population_criteria = 25000000

    # Apply conditions to filter the DataFrame
    big_countries = data[(data["area"] >= area_criteria) | (data["population"] >= population_criteria)]

    # Extract relevant columns: name, population, and area
    big_countries = big_countries[["name", "population", "area"]]
    return big_countries

# Defines the main function
def __main__():
    # Call the functions and load data and pass data
    data = load_data()
    display_data_structure(data)
    big_countries = identify_big_countries(data)

    # Output the DataFrame of big countries
    print("\nBig countries based on area or population criteria:")
    print(big_countries)


# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
