#####################
## Dalton Murray    #
## 02/05/2024       #
## Notes            #
#####################
import sys # Required for system functions

import os
import pandas as pd # Import the pandas library and sets an alias to pa
import numpy as np

# Defines the __main__ function
def __main__():

    # series_example = pd.Series([1, 3, 5, 7, 9])
    # data = {"Name": ["Anna", "Bob", "Cathy"], "Age": [28, 34, 29]}
    # df_example = pd.DataFrame(data)

    # print(series_example.head(2))
    # print(df_example)
    # print(df_example.head(2))
    # print(df_example.tail(2))
    # print(len(df_example))
    # print(len(series_example))
    # print(df_example.columns)
    # print(len(df_example.columns))

    database = "./"
    bostonHousing_df = pd.read_csv(os.path.join(database, "BostonHousing.csv"))
    # pd.read_excel()
    print(len(bostonHousing_df)) # Length/rows of file
    print(bostonHousing_df.shape) # Rows and columns
    print(bostonHousing_df.head(1))
    print(bostonHousing_df.describe())
    print(bostonHousing_df.dtypes)
    # bostonHousing_df = bostonHousing_df.rename(columns={"Cat. MEDV": "CAT_MEDV"})
    print(bostonHousing_df.max())
    print(bostonHousing_df.min())
    print(bostonHousing_df.mean())
    print(bostonHousing_df["AGE"]) # Series
    print(bostonHousing_df[["AGE", "CRIM"]]) # Dataframe
    df_new = bostonHousing_df[["AGE", "CRIM"]]
    print(df_new.columns)
    print(bostonHousing_df.head())
    print(bostonHousing_df.iloc[4])
    print(bostonHousing_df[0:5])
    bostonHousing_df["new_one"] = bostonHousing_df["CRIM"] * bostonHousing_df["TAX"]
    print(bostonHousing_df.head())
    del bostonHousing_df["new_one"]
    print(bostonHousing_df.columns)
    bostonHousing_df.iloc[0:3, 3] = np.nan_to_num
    print(bostonHousing_df.head())
    # df = bostonHousing_df.dropna(how="any")
    df = bostonHousing_df.fillna(value = 5)
    print(df.head())
    print(bostonHousing_df.groupby("CHAS").mean())
    # df1 = bostonHousing_df.loc[:100]
    # df2 = bostonHousing_df.loc[100:]
    df1 = bostonHousing_df.iloc[:, 0:3]
    df2 = bostonHousing_df.iloc[:, 6:9]
    print(df1, df2)
    print(df1.shape)
    print(df2.shape)
    df = pd.concat([df1, df2], axis = 1)
    print(df.shape)
    print(bostonHousing_df[bostonHousing_df["AGE"] < 5]["AGE"])



# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly


