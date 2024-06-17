#####################
## Dalton Murray    #
## 02/14/2024       #
## Notes            #
#####################
import sys # Required for system functions

import os
import pandas as pd # Import the pandas library and sets an alias to pa
import numpy as np
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt

# Defines the __main__ function
def __main__():

    # datafolder = "./"
    # file_name = "./Week05/world.csv"
    # df = pd.read_csv(os.path.join(datafolder, file_name))
    # print(df)
    # df_new = df[(df.area >= 3000000) | (df.population >= 2500000)][["name", "population", "area"]]
    # print(df_new)

    # datafolder = "./"
    # file_name = "./Week05/products.csv"
    # df = pd.read_csv(os.path.join(datafolder, file_name))
    # df_new = df[(df.low_fats == "Y") & (df.recyclable == "Y")][["product_id"]].rename(columns = {"product_id":"id"})
    # print(df_new)

    # datafolder = "./"
    # file_name = "./Week05/orders.csv"
    # file_name2 = "./Week05/customers.csv"
    # orders = pd.read_csv(os.path.join(datafolder, file_name))
    # customers = pd.read_csv(os.path.join(datafolder, file_name2))
    # df = pd.DataFrame()
    # df["customers"] = customers[~(customers.id.isin(orders.customerId))][["name"]]
    # print(df)

    # datafolder = "./"
    # file_name = "./Week05/views_modified.csv"
    # views = pd.read_csv(os.path.join(datafolder, file_name))
    # df = views[(views["viewer_id"] == views["author_id"])][["author_id"]].rename(columns = {"author_id":"id"}).sort_values(by = ["id"]).drop_duplicates()
    # print(df)

    # datafolder = "./"
    # file_name = "./Week05/tweets.csv"
    # tweets = pd.read_csv(os.path.join(datafolder, file_name))
    # invalid = [(tweets["content"].str.len() > 15)][["tweet_id"]]
    # print(invalid)

    # datafolder = "./"
    # file_name = "./Week05/employees_bonus.csv"
    # employees = pd.read_csv(os.path.join(datafolder, file_name))
    # # employees["bonus"] = employees["salary"]
    # # employees[(employees["employee_id"] % 2 == 0) | (employees["name"].str.startswith("M"))]["bonus"] = 0
    # employees["bonus"] = employees.apply(lambda x: x["salary"] if x["employee_id"] % 2 and not x["name"].startswith("M") else 0, axis = 1)
    # print(employees)

    # datafolder = "./"
    # file_name = "./Week05/employees_bonus.csv"
    # employees = pd.read_csv(os.path.join(datafolder, file_name))
    # bonus = employees.salary.where (
    #     (employees.employee_id % 2 == 1) & (~employees.name.str.startswith("M")),
    # )
    # print(bonus)

    # datafolder = "./"
    # file_name = "./Week05/users.csv"
    # users = pd.read_csv(os.path.join(datafolder, file_name))
    # # users["name"] = users["name"].str.upper()
    # users["name"] = users["name"].apply(lambda x: x.capitalize())
    # print(users)

    datafolder = "./"
    file_name = "./Week05/users_email.csv"
    users = pd.read_csv(os.path.join(datafolder, file_name))
    pattern = r"^[a-zA-Z][a-zA-Z_.-0-9]*\@leetcode\.com$"
    users = users[users["mail"].str.match(pattern)]
    print(users)

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
