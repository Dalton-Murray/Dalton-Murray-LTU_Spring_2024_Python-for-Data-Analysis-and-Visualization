#####################
## Dalton Murray    #
## 03/18/2024       #
## Notes            #
#####################
import sys # Required for system functions

import os
import time
import pandas as pd # Imports the pandas library and sets an alias to pa
import numpy as np # Imports the numpy library and sets an alias to np
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt
import seaborn as sns # Imports seaborn and sets an alias to sns

# Defines the __main__ function
def __main__():

    sns.set(style="darkgrid")

    # tips = sns.load_dataset("tips")
    # tips.head()

    # tips = sns.load_dataset("tips")
    # sns.histplot(data = tips, x = "total_bill")
    # plt.title("Total Bill Histogram")
    # plt.xlabel("Total Bill ($)")
    # plt.ylabel("Frequency")
    # plt.show()

    # data = {"Apples": 50, "Oranges":30, "Bananas":20}
    # names = list(data.keys())
    # values = list(data.values())
    # plt.bar(names, values)
    # plt.title("Fruit Consumption")
    # plt.show()

    # sns.scatterplot(x = "total_bill", y = "tip", data = tips)
    # plt.title("Total Bill vs Tip")
    # plt.xlabel("Total Bill")
    # plt.ylabel("Tip")
    # plt.show()

    # flights = sns.load_dataset("flights")
    # flights.head()

    # flights = sns.load_dataset("flights")
    # flights_pivot = flights.pivot("month", "year", "passengers")
    # flights_pivot.head()

    # plt.figure(figsize = (12, 6))
    # sns.lineplot(data = flights_pivot)
    # plt.title("Monthly Passengers Over the Years")
    # plt.xlabel("Month")
    # plt.ylabel("Number of Passenbers")
    # plt.xticks(rotation = 45)

    # tips = sns.load_dataset("tips")
    # plt.figure(figsize = (8, 6))
    # sns.barplot(x = "day", y = "tip", data = tips)
    # plt.title("Average Tip Amount by Day of the Week")


    # sns.scatterplot(x="total_bill", y="tip", hue="time", data=tips, palette="Set1")
    # plt.title("Total Bill vs Tip by Smoking")
    # plt.show()
    # # Changing the plot style
    # sns.set_style("whitegrid")
    # sns.barplot(x="day", y="tip", data=tips, palette="viridis")
    # plt.title("Bar Plot with Custom Style")
    # plt.show()

    # tips = sns. load_dataset('tips')
    # # Create a histogram
    # sns.histplot(tips['total_bill'], kde=False, color='blue', bins=20)
    # plt.title('Histogram of Total Bills')
    # plt.xlabel('Total Bill ($)')
    # plt.ylabel('Frequency')
    # plt.show()

    # sns.kdeplot(tips['tip'], shade=True, color='red')
    # plt.title('KDE Plot of Total Bills')
    # plt.xlabel('Total Bill ($)')
    # plt.show()

    # # Create a bar plot
    # sns.barplot(x='day', y='total_bill', data=tips, palette='autumn')
    # plt.title('Average Total Bill by Day')
    # plt.xlabel('Day of the Week')
    # plt.ylabel('Average Total Bill ($)')
    # plt.show()

    # sns.violinplot(x='day', y='total_bill', data=tips)
    # plt.title('Violin Plot of Total Bills by Day')
    # plt.xlabel('Day of the Week')
    # plt.ylabel('Total Bill ($)')
    # plt.show()

    # sns.pairplot(tips, hue = "sex", palette='pastel')
    # plt.show()

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly





