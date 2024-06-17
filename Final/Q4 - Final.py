#####################
## Dalton Murray    #
## 04/29/2024       #
## Q4               #
#####################
import sys

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Defines the load_data function
def load_data():
    # Load the scores.csv file and sets it to the data dataframe
    data = pd.read_csv("scores.csv")
    # Returns the data dataframe
    return data

# Defines the display_data_structure function and takes in data
def display_data_structure(data):
    # Print the first few rows to get a sense of the data format and contents
    print("First few rows of the DataFrame:")
    print(data.head())

# Defines the rank_scores function and takes in data
def rank_scores(data):
    # Sort the DataFrame by "score" in descending order to prepare for ranking
    data_sorted = data.sort_values(by="score", ascending=False)

    # Use pandas" rank() method to rank scores; method="dense" ensures that ranks are consecutive without gaps
    data_sorted["rank"] = data_sorted["score"].rank(method="dense", ascending=False)

    # Returns the data_sorted dataframe
    return data_sorted

# Defines the output_results function and takes in data_sorted
def output_results(data_sorted):
    # Select only the "score" and "rank" columns to output
    results = data_sorted[["score", "rank"]]
    print("\nRanked scores:")
    print(results)

# Defines the main function
def __main__():
    """Main function to run the analysis."""
    data = load_data()
    display_data_structure(data)
    data_sorted = rank_scores(data)
    output_results(data_sorted)

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
