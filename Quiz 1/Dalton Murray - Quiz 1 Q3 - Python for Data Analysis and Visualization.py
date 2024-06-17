#####################
## Dalton Murray    #
## 01/22/2024       #
## Quiz 1 Q3        #
#####################
import sys # Required for system functions

# Defines the __main__ function
def __main__():

    for number in range(1, 51):
        # print(number) # Verifies that I am taking the numbers 1 - 50
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)
        else:
            pass
# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly