#####################
## Dalton Murray    #
## 03/11/2024       #
## Notes            #
#####################
import sys # Required for system functions

import os
import pandas as pd # Import the pandas library and sets an alias to pa
import numpy as np
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt

# Defines the __main__ function
def __main__():

    # # lambda arguments: expression
    # add = lambda x, y: x + y
    # print(add(4, 5), add(6, 7))

    # my_list = [(0.56, "banana"), (1.99, "apple"), (3.99, "strawberry")]
    # my_list.sort(key = lambda x: x[1])
    # print(my_list)
    # t = [4, 6, 34, 2, 10]
    # t.sort()
    # print(t)

    # numbers = [11, 20, 13, 411, 5, 16]
    # even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    # print(even_numbers)

    # # Filter Function
    # # filter()
    # class Product():
    #     def __init__(self, name, price):
    #         self.name = name
    #         self.price = price
    # products = [Product("Apple", 1.99), Product("Banana", 0.56), Product("Orange", 0.99)]
    # expensive_products = list(filter(lambda p: p.price > 1, products))
    # expensive_product_names = [p.name for p in expensive_products]
    # print(expensive_product_names)
    # for product in expensive_products:
    #     print(f"Name: {product.name}, Price: {product.price}")

    # # Map
    # # map(function, iterable, ...)
    # numbers = [1, 2, 3, 4, 5, 6]
    # squared = list(map(lambda x: x ** 2, numbers))
    # print(squared)

    # nums1 = [2, 3, 4, 5]
    # nums2 = [5, 7, 2, 3]
    # summed = list(map(lambda x, y: x + y, nums1, nums2))
    # print(summed)

    # ZIP
    # list1 = [0.99, 1.99, 0.56]
    # list2 = ["apple", "orange", "banana"]
    # zipped = zip(list1, list2)
    # # zipped = list(zip)
    # # dict_zipped = dict(zipped)
    # # print(dict_zipped)
    # names, prices = zip(*zipped)
    # print(names)
    # print(prices)

    # nums1 = [2, 3, 4]
    # nums2 = [5, 6, 7, 8]
    # zipped = zip(nums1, nums2)
    # print(list(zipped))

    # product_names = ["Product A", "Product B", "Product C"]
    # prices = [100, 150, 200]
    # df = pd.DataFrame(list(zip(product_names, prices)), columns = ["Product", "Price"])
    # zipped = dict(zip(product_names, prices))
    # print(df)

    # # Enumerate
    # nums = ["a", "b", "c"]
    # # enumerate(nums)
    # for index, name in enumerate(nums, start = 1):
    #     print(name, index)
    # # print(list(enumerate(nums, start = 1)))
    # print(dict(enumerate(nums, start = 1)))

    

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly




