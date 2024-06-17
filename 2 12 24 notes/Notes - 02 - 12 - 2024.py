#####################
## Dalton Murray    #
## 02/12/2024       #
## Notes            #
#####################
import sys # Required for system functions

import os
import pandas as pd # Import the pandas library and sets an alias to pa
import numpy as np
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt

# Defines the __main__ function
def __main__():

    # student_data=[[1, 15], [2, 11], [3, 11], [4, 20]]
    # student_df = pd.DataFrame(student_data, columns = ("id", "age"))
    # print(student_df)

    # df = pd.read_csv("./Archive/players.csv")
    # n_row, n_col = df.shape
    # print(n_row, n_col)
    # print(df.head(3))

    # df = pd.read_csv("./Archive/students_sample.csv")
    # df1 = df.query("student_id == 101")[["name", "age"]]
    # print(df1)
    # df1 = df.loc[df.student_id == 101, ["name", "age"]]
    # print(df1)
    # df1 = df[df["student_id"] == 101][["name", "age"]]
    # print(df1)

    # df = pd.read_csv("./Archive/employees.csv")
    # df["bonus"] = df["salary"].apply(lambda x: x * 2 if x <= 70000 else x * 1.5)
    # print(df)

    # t = [1, 2, 3, 4]
    # list = [i * 2 for i in t]
    # print(list)

    # df = pd.read_csv("./Archive/customers.csv")
    # print(df)
    # df.drop_duplicates(subset = "email", keep = "first", inplace = True)
    # print(df)

    # df = pd.read_csv("./Archive/students_sample.csv")
    # print(df)
    # df = df.dropna(subset = "name", inplace = True)

    # df = pd.read_csv("./Archive/employees.csv")
    # print(df)
    # df["salary"] = df["salary"].apply(lambda x: x * 1.05 if x < 90000 else x)
    # print(df)

    # df = pd.read_csv("./Archive/students_sample.csv")
    # df = df.rename(columns = {"student_id":"id", "name":"first_name", "age":"age_in_years"})
    # print(df)

    # df = pd.read_csv("./Archive/students_sample.csv")
    # print(df["age"].dtype)
    # df["age"] = df["age"].astype("float")
    # print(df["age"].dtype)

    # df = pd.read_csv("./Archive/products_with_missing.csv")
    # print(df)
    # df["quantity"] = df["quantity"].fillna(0)
    # print(df)

    # df1 = pd.read_csv("./Archive/df1.csv")
    # df2 = pd.read_csv("./Archive/df2.csv")
    # df = pd.concat([df1, df2], axis = 0)
    # print(df)
    # df3 = df1[["student_id", "name"]]
    # df4 = df1[["age"]]
    # df5 = pd.concat([df3, df4], axis = 1)
    # print(df3)
    # print(df4)
    # print(df5)

    # df = pd.read_csv("./Archive/weather.csv")
    # print(df)
    # df2 = df.pivot(index = "month", columns = "city", values = "temperature")
    # print(df2)

    df = pd.read_csv("./Archive/report.csv")
    print(df)
    df2 = df.melt(df, id_var = "product", var_name = "quarter", value_vars = ["quarter_1", "quarter_2", "quarter_3", "quarter_4"], value_name = "sales")
    print(df2)


# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly


