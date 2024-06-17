#####################
## Dalton Murray    #
## 02/26/2024       #
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
    # file_name = "./Week05/patients.csv"
    # patients = pd.read_csv(os.path.join(datafolder, file_name))
    # DIAB1 = patients.fillna("3 DIAB1")
    # # DIAB1 = DIAB1[(DIAB1["conditions"].str.contains("DIAB1")) | (DIAB1["conditions"].str.contains(" DIAB1"))]
    # # print(patients)
    # pattern = r"^[A-Z0-9 ]*\bDIAB1[A-Z0-9 ]*$"
    # DIAB1 = DIAB1[DIAB1["conditions"].str.match(pattern)]
    # print(DIAB1)

    # datafolder = "./"
    # file_name = "./Week05/files_content.csv"
    # files = pd.read_csv(os.path.join(datafolder, file_name))
    # n_bull = files[files["content"].str.contains(" bull ")]["file_name"].nunique()
    # n_bear = files[files["content"].str.contains(" bear ")]["file_name"].nunique()
    # data = {
    #     "word":["bear", "bull"],
    #     "count":[n_bear, n_bull]
    #     }
    # df = pd.DataFrame(data)
    # print(n_bull, n_bear)
    # print(df)

    # datafolder = "./"
    # file_name = "./Week05/employees_bonus.csv"
    # employee = pd.read_csv(os.path.join(datafolder, file_name))
    # employee["rank"] = employee["salary"].rank(method = "dense", ascending = False)
    # employee["rank"] = employee["rank"].astype("int")
    # n = 6
    # df = pd.DataFrame()
    # df[f"getNthHighestSalary({n})"] = (employee[employee["rank"] == n]["salary"] if n in employee["rank"] else [None])
    # print(df)

    """
    Table: Employee

    +-------------+------+
    | Column Name | Type |
    +-------------+------+
    | id          | int  |
    | salary      | int  |
    +-------------+------+
    id is the primary key (column with unique values) for this table.
    Each row of this table contains information about the salary of an employee.

    Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

    The result format is in the following example.

    Example 1:
    Input:
    Employee table:
    +----+--------+
    | id | salary |
    +----+--------+
    | 1  | 100    |
    | 2  | 200    |
    | 3  | 300    |
    +----+--------+
    Output:
    +---------------------+
    | SecondHighestSalary |
    +---------------------+
    | 200                 |
    +---------------------+
    """

    datafolder = "./"
    file_name = "./Week05/employees_bonus.csv"
    employee = pd.read_csv(os.path.join(datafolder, file_name))

    secondHighestSalary = employee['salary'].nlargest(2).iloc[-1] if len(employee) > 1 else None
    resultSecondHighest = pd.DataFrame({'SecondHighestSalary': [secondHighestSalary]})
    print(resultSecondHighest)

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly


