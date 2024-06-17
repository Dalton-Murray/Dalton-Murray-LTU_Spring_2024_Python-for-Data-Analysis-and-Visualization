#####################
## Dalton Murray    #
## 01/29/2024       #
## Notes            #
#####################
import sys # Required for system functions

# Defines the __main__ function
def __main__():

    # x, y = 10, 12
    # t = my_function(x, y)
    # print(t)

    x, y, z = 7, 8, 12
    t = summation(x, y, z, 10, 11)
    print(t)

    x, y, z, = 0, 9, 45
    print_details(x, y, z, name = "Alice", age = 30, city = "New York", occupation = "Engineer")

# def my_function(par1, par2 = 30): # `par2 = 30` sets default unless provided
#     return par1 + par2

def summation(*args, **kwargs):
    total = 0
    for item in args:
        total += item
    return total

def print_details(*args, **kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    total = 0
    for item in args:
        total += item
    print(total)

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly