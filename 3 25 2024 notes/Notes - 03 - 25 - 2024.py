#####################
## Dalton Murray    #
## 03/25/2024       #
## Notes            #
#####################
import sys # Required for system functions

import pandas as pd # Imports the pandas library and sets an alias to pa
import numpy as np # Imports the numpy library and sets an alias to np
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt
import seaborn as sns # Imports seaborn and sets an alias to sns

# Defines the __main__ function
def __main__():

    sales_data = pd.read_csv("./Sales_Data.csv")
    customer_data = pd.read_csv("./Customer_Data.csv")
    # print(sales_data.dtypes)
    # print(customer_data.dtypes)



# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
