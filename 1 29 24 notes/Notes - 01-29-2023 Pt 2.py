#####################
## Dalton Murray    #
## 01/29/2024       #
## Notes            #
#####################
import sys # Required for system functions

import numpy as npy # Imports numpy library and sets an alias to npy
import matplotlib as mplib # Imports matplotlib library and sets an alias to mplib

# Defines the __main__ function
def __main__():

    # open()
    # read()
    # reeadline()
    # readlines()
    # write()
    # writelines()
    # close()
    # with

    # file = open("new.txt", "w") # Creates a new file if does not exit and opens in write
    file = open("example.txt", "r") # Opens example.txt in read mode
    lines = file.readlines() # Reads all lines of file
    file.close() # Closes the open file

    print(lines)
    print(type(lines))

    file = open("new.txt", "w") # Opens new.txt in write mode, will overwrite contents
    file.write("Hello World!\n")
    file.close()

    file = open("new.txt", "a") # Opens new.txt and appends to file
    file.write("Hello World! 2\n")
    file.close()

    with open("sample2.txt", "w") as file: # Automatically handles opening and closing using with
        file.write("Hello Everyone!")


    try:
        with open("unknown.txt", "r") as file:
            contents = file.read()
    except FileNotFoundError:
        print("Could not find file please check directory")
    else:
        print(contents)


    try:
        x = int(input("Please enter value: "))
        y = int(input("Please enter value 2: "))
        result = x/y
    except ZeroDivisionError:
        print("You were about to divide by 0, please check your inputs")
    except ValueError:
        print("Please only use whole numbers in your input")
    else:
        print("Results = ", result)
    finally:
        print("Goodbye")


# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly