#####################
## Dalton Murray    #
## 01/22/2024       #
## Quiz 1 Q2        #
#####################
import sys # Required for system functions

# Defines the __main__ function
def __main__():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squared_numbers = []

    for item in numbers:
        square = item ** 2
        squared_numbers.append(square)

    print(squared_numbers)

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly