#####################
## Dalton Murray    #
## 03/20/2024       #
## Notes            #
#####################
import sys # Required for system functions

import pandas as pd # Imports the pandas library and sets an alias to pa
import numpy as np # Imports the numpy library and sets an alias to np
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt
import seaborn as sns # Imports seaborn and sets an alias to sns

# Defines the __main__ function
def __main__():

    # # superstore = sns.load_dataset("./Sample - Superstore.csv")
    # superstore = pd.read_csv("new.csv")
    # superstore.head(1)
    # superstore.shape()
    # superstore.describe()
    # superstore["Order Date"] = pd. to_datetime(superstore["Order Date"])
    # superstore.describe()

    # superstore = pd.read_csv("./SampleSuperstore.csv")
    # superstore["Order Date"] = pd.to_datetime(superstore["Order Date"])
    # sns.lineplot(data = superstore["Sales"])
    # # plt.show()
    # superstore.set_index("Order Date", inplace = True)
    # # plt.show()
    # superstore_monthly = superstore["Sales"].resample("M").sum()
    # # print(superstore_monthly)
    # plt.figure(figsize = (14, 6))
    # plt.title("Monthly Sales Over Time")
    # plt.xlabel("Date")
    # plt.ylabel("Sum of Sales")
    # sns.lineplot(data = superstore_monthly)
    # plt.show()

    # superstore = pd.read_csv("./SampleSuperstore.csv")
    # superstore["Order Date"] = pd.to_datetime(superstore["Order Date"])
    # superstore.set_index("Order Date", inplace = True)
    # print(set(superstore["Category"]))
    # print(len(set(superstore["Category"])))
    # whole_cat_sale = superstore.groupby("Category")["Sales"].sum()
    # print(whole_cat_sale)
    # sns.barplot(data = whole_cat_sale)
    # plt.show()

    # superstore = pd.read_csv("./SampleSuperstore.csv")
    # # sns.barplot(x = "Category", y = "Sales", data = superstore, estimator = sum)
    # # plt.show()
    # sns.boxplot(x = "Category", y = "Sales", data = superstore, showfliers = False)
    # plt.show()

    # superstore = pd.read_csv("./SampleSuperstore.csv")
    # correlation = superstore[["Sales", "Quantity", "Discount", "Profit"]].corr()
    # print(correlation)
    # sns.heatmap(correlation, annot = True)
    # plt.show()

    # superstore = pd.read_csv("./SampleSuperstore.csv")
    # sns.lmplot(x = "Sales", y = "Profit", data = superstore)
    # plt.show()

    # superstore = pd.read_csv("./SampleSuperstore.csv")
    # sns.stripplot(x = "Category", y = "Sales", data = superstore)
    # plt.show()

    # superstore = pd.read_csv("./SampleSuperstore.csv")
    # sns.pointplot(x = "Category", y = "Profit", data = superstore, hue = "Region")
    # plt.show()

    superstore = pd.read_csv("./SampleSuperstore.csv")
    sns.violinplot(x = "Category", y = "Sales", data = superstore, palette = Set1)
    plt.show()

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
