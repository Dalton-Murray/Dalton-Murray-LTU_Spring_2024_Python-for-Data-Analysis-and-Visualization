#####################
## Dalton Murray    #
## 04/29/2024       #
## Q6               #
#####################
import sys

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def __main__():
    # Generate an array x of 100 points linearly spaced between -2π and 2π
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

    # Create a second array y using the cosine function applied to each element of x
    y = np.cos(x)

    # Create a third array z where each element is:
    # - the cosine of the element in y multiplied by -1 if the corresponding x value is less than 0
    # - otherwise, just the cosine value
    z = np.where(x < 0, -np.cos(y), np.cos(y))

    # Plot x vs y using a blue line
    plt.plot(x, y, label="Cosine Curve (y = cos(x))", color="blue")

    # On the same graph, plot x vs z using a red line only for the segments of x where x is greater than 0
    # This includes filtering both x and z arrays where x > 0
    plt.plot(x[x > 0], z[x > 0], label="Modified Cosine Curve (x > 0)", color="red")

    # Add a legend to differentiate between the two curves
    plt.legend()

    # Label the axes
    plt.xlabel("x values")
    plt.ylabel("y and z values")

    # Title the plot
    plt.title("Comparison of Cosine Curves")

    # Display the plot
    plt.show()

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
