#####################
## Dalton Murray    #
## 03/13/2024       #
## Notes            #
#####################
import sys # Required for system functions

import os
import time
import pandas as pd # Imports the pandas library and sets an alias to pa
import numpy as np # Imports the numpy library and sets an alias to np
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt

# Defines the __main__ function
def __main__():

    # t = [4, 8.0, "ft", [4, 6, 7]]
    # print(t[3])

    # for i in range(1, 5):
    #     print(i)

    # size = 1_000_000
    # python_list = list(range(size))
    # # print(python_list(size))
    # numpy_array = np.arange(size)
    # # print(numpy_array[:10])

    # start_time = time.time()
    # sum_list = sum(python_list)
    # end_time = time.time()
    # print(end_time - start_time)

    # start_time = time.time()
    # sum_array = np.sum(numpy_array)
    # end_time = time.time()
    # print(end_time - start_time)

    # pl = list(range(12))
    # pl2 = [i ** 3 for i in pl]
    # # for i in range(len(pl)):
    # #     pl2.append(pl[i] * pl[i])
    # print(pl2)

    # nl = np.array(pl)
    # print(nl)
    # print(type(pl))
    # print(type(nl))

    # nl = np.arange(12)
    # nl2 = nl ** 3
    # print(nl2)

    # zz = np.zeros([3, 3])
    # oo = np.ones(12)
    # print(zz, oo)

    # tt = np.linspace(0, 10, 100)
    # xx = np.sin(tt)
    # # plt.plot(tt, xx)
    # # plt.show()
    # print(tt)
    # print(xx)

    # zz = np.zeros([2, 3])
    # oo = np.ones([2, 3]) + 6
    # print(zz + 2 * oo)
    # print(zz.shape[0])

    # np.sum,
    # np.mean,
    # np.std,
    # np.min,
    # np.max

    # nl = np.arange(12)
    # print(nl[:-1])
    # print(nl[:3:])
    # print(nl[::2])

    # sales_data = np.array([[200, 1.20], [450, 1.35], [300, 1.50], [600, 1.10]])
    # # print(sales_data[:, 0] > 200)
    # # high_sales = sales_data[sales_data[:, 0] > 300]
    # high_sales = sales_data[sales_data[:, 1] > 1.2]
    # print(high_sales)

    # quarterly_sales = np.array([
    #     [1500, 2000, 2500, 2200],
    #     [4000, 4500, 4800, 4700],
    #     [3000, 3100, 3200, 3100],
    #     [1000, 1100, 1300, 1200]
    # ])
    # product_b_sales = quarterly_sales[1, :]

    nl = np.arange(12)
    n2 = nl.reshape((4, 3))
    # print(n2)
    print(n2.transpose())

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly





