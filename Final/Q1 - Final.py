#####################
## Dalton Murray    #
## 04/29/2024       #
## Q1               #
#####################
import sys

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Defines the load_data function
def load_data():
    # Imports sales_data.csv as a dataframe called data
    data = pd.read_csv("sales_data.csv")
    # Returns the dataframe from reading sales_data
    return data

# Defines the display_data_structure function and takes in data
def display_data_structure(data):
    print("First 10 rows of the dataset:")
    # Prints out the first 10 rows of data
    print(data.head(10))
    print("\nColumn names:")
    # Prints out the columns in the data dataframe
    print(data.columns)

# Defines the descriptive_analysis function and takes in data
def descriptive_analysis(data):
    print("\nDescriptive statistics for numerical columns:")
    # Performs basic statistics on the data dataframe using .describe
    print(data.describe())
    print("\nFrequency counts for categorical columns:")
    # Gets the value counts of customer_type
    print(data["Customer_Type"].value_counts())

# Defines the visual_summaries function and takes in data
def visual_summaries(data):
    # For each column, determine the appropriate plot type based on data type
    # Determine the appropriate plot type based on data type
    for column in data.columns:
        plt.figure(figsize=(10, 4))

        # If it's an object do a countplot
        if data[column].dtype == 'object':
            # For categorical data, use count plots
            sns.countplot(x=column, data=data)
            plt.title(f'Count Plot of {column}')
            plt.xticks(rotation=45)

        # If it's an int64 or float64 make a histplot and boxplot
        elif data[column].dtype in ['int64', 'float64']:
            plt.subplot(1, 2, 1)
            sns.histplot(data[column], kde=True)
            plt.title(f'Distribution of {column}')

            plt.subplot(1, 2, 2)
            sns.boxplot(y=column, data=data)
            plt.title(f'Box Plot of {column}')

        # If it's datetime make a time series plot
        elif data[column].dtype == 'datetime64[ns]':
            data[column].value_counts().sort_index().plot()
            plt.title(f'Time Series Trend of {column}')

        # Sets layout to tight
        plt.tight_layout()
        # Shows plots
        plt.show()

# Defines the relationship_analysis function and takes in data
def relationship_analysis(data):
    # Calculates correlation matrix using .corr
    correlation_matrix = data.corr()
    print("\nCorrelation matrix:")
    # Prints out the correlation matirx
    print(correlation_matrix)
    # Make a heatmap of the data
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix Heatmap")
    plt.show()

# Defines the preliminary_visualization function and takes in data
def preliminary_visualization(data):
    # Scatter plot for Units Sold vs. Unit Price by Customer Type
    sns.scatterplot(x="Unit_Price", y="Units_Sold", hue="Customer_Type", data=data)
    plt.title("Units Sold vs Unit Price by Customer Type")
    plt.show()

    # Additional Visualization: Boxplot for Unit Price by Customer Type
    sns.boxplot(x="Customer_Type", y="Unit_Price", data=data)
    plt.title("Unit Price by Customer Type")
    plt.show()

    # Time series trend of sales volume
    data["Date"] = pd.to_datetime(data["Date"])
    data.sort_values("Date", inplace=True)
    data.set_index("Date")["Units_Sold"].plot()
    plt.ylabel("Units Sold")
    plt.title("Sales Volume Over Time")
    plt.show()

# Defines __main__
def __main__():
    # Main function to get data and pass to other functions and call them
    data = load_data()
    display_data_structure(data)
    descriptive_analysis(data)
    visual_summaries(data)
    relationship_analysis(data)
    preliminary_visualization(data)

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
