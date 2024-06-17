#####################
## Dalton Murray    #
## 01/22/2024       #
## Quiz 1 Q1        #
#####################
import sys # Required for system functions

import math #Requires for pi

# Defines the __main__ function
def __main__():


    radiusOfCircle = 5
    print(calculate_circle_area(radiusOfCircle))


def calculate_circle_area(radiusOfCircle):
    area = (math.pi * radiusOfCircle) * radiusOfCircle
    return area


# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly