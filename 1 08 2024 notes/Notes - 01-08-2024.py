#####################
## Dalton Murray    #
## 01/08/2024       #
## Notes            #
#####################
import sys # Required for system variables

# Defines the __main__ function
def __main__():
    print("Hello world")

    #10 - Integer
    #10.1 - Float
    #"Hello World!" - String
    #'Hello World!' - String
    #True/False - Boolean

    numberTen = 10
    print(numberTen)

    print(f"Hello World! 1 - {numberTen}")
    print("Hello World! 2 -", numberTen)

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits