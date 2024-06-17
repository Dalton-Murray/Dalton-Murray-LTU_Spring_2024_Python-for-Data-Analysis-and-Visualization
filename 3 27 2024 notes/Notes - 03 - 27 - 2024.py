#####################
## Dalton Murray    #
## 03/27/2024       #
## Notes            #
#####################
import sys # Required for system functions

import pandas as pd # Imports the pandas library and sets an alias to pa
import numpy as np # Imports the numpy library and sets an alias to np
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt
import seaborn as sns # Imports seaborn and sets an alias to sns

# Defines the __main__ function
def __main__():

    amazon = pd.read_csv("./AmazonSaleReport.csv")

    # print(amazon.dtypes)
    # print(amazon.describe())
    # print(amazon["Date"])

    amazon["Date"] = pd.to_datetime(amazon["Date"])
    # amazon.set_index("Date")["Amount"].plot()
    # amazon.groupby("Date")["Amount"].sum().plot()

    # rolling_avg = amazon.groupby("Date")["Amount"].sum().rolling(window = "3D").mean()
    # print(rolling_avg)
    # rolling_avg.plot()

    #cumulative_sum = amazon.groupby("Date")["Amount"].sum().expanding().sum()

    # cumulative_avg = amazon.groupby("Date")["Amount"].sum().expanding().mean()

    # weekly_sales = amazon.set_index("Date").resample("M")["Amount"].sum()
    # weekly_sales.plot()

    # df_query = amazon[amazon["Sale_Cat"] == "Large"]
    

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
