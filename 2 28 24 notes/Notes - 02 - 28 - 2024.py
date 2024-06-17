#####################
## Dalton Murray    #
## 02/28/2024       #
## Notes            #
#####################
import sys # Required for system functions

import os
import pandas as pd # Import the pandas library and sets an alias to pa
import numpy as np
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt

# Defines the __main__ function
def __main__():

    datafolder = "./"
    file_name = "./Week05/employees_bonus.csv"
    employee = pd.read_csv(os.path.join(datafolder, file_name))

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly



