#####################
## Dalton Murray    #
## 01/31/2024       #
## Notes            #
#####################
import sys # Required for system functions

import numpy as np # Imports numpy library and sets an alias to np
import matplotlib as mplib # Imports matplotlib library and sets an alias to mplib
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt
from matplotlib.widgets import Slider, Button # Imports the slider and button from widgets for interactivity

# Defines the __main__ function
def __main__():

    x = [1, 2, 3, 4]
    y = [1, 4, 9, 16]

    fig, ax = plt.subplots()

    # ax.plot(x, y, label = "Data from list")
    # ax.set_title("Simple plot")
    # ax.set_xlabel("x values")
    # ax.set_ylabel("y values")
    # plt.show()

    # x_array = np.array([1, 2, 3, 4])
    # y_array = np.array([1, 4, 9, 16])
    # ax.plot(x_array, y_array, label = "Data from array", linestyle="--")

    # ax.set_title("Plotting with Lists and Numpy Arrays")
    # ax.set_xlabel("x values")
    # ax.set_ylabel("y values")
    # ax.legend()
    # plt.show()

    # plt.plot(x, y, color = "red", linestyle = "--", linewidth = 2)
    # ax.set_title("Customized Line Plot")
    # ax.set_xlabel("x values")
    # ax.set_ylabel("y values")
    # plt.grid(True)
    # ax.legend()
    # plt.show()

    # categories = ["Category A", "Category B", "Category C"]
    # values = [10, 20, 15]
    # plt.bar(categories, values)
    # plt.xlabel("Categories")
    # plt.ylabel("Values")
    # plt.title("Bar chart for categorical data")
    # plt.grid(True)
    # plt.show()

    # data = np.random.normal(0, 1, 1000) # Generate sample data, also different types of random binomial, rand, uniform rather than just normal
    # plt.hist(data, bins = 30)
    # plt.xlabel("Value")
    # plt.ylabel("Frequency")
    # plt.title("Histogram for Frequency Distribution")
    # plt.show()

    # np.random.seed(0)
    # data = np.random.uniform(3, 7, 100)
    # plt.hist(data, bins = 30)
    # plt.xlabel("Value")
    # plt.ylabel("Frequency")
    # plt.title("Histogram for Frequency Distribution")
    # plt.show()

    # x = np.random.rand(50)
    # y = np.random.rand(50)
    # plt.scatter(x, y)
    # plt.xlabel("X value")
    # plt.ylabel("Y value")
    # plt.title("Scatter plot for bivariate data")
    # plt.grid(True)
    # plt.show()

    x = np.random.rand(50)
    y = np.random.rand(50)
    # Color array
    colors = np.random.rand(50)  # Generate random colors
    # Size array (scaled)
    sizes = 1000 * np.random.rand(50)
    # Create customized scatter plot
    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
    # Add a colorbar
    plt.colorbar()
    # Customize with labels and title
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.title('Customized Scatter Plot')
    # Show the plot
    plt.show()

    # ax.plot([0, 1, 2], [10, 20, 30])
    # ax.set_xticks([0, 1, 2])
    # ax.set_yticks([10, 20, 30, 40])
    # ax.grid(True, which = "both", axis="both", color="gray", linestyle="--", linewidth = 0.5)
    # ax.set_xlim(0, 2)
    # ax.set_ylim(10, 40)
    # plt.show()

# # Setup a plot
# fig, ax = plt.subplots()
# plt.subplots_adjust(left=0.25, bottom=0.25)  # Make room for the slider
# def f (w, x):
#     return np.sin(w*x)
# # Assume we have a function f that depends on a parameter 'a'
# a0 = 1
# x = np.arange(0, 2*np.pi, 0.001)
# y = f(a0, x)
# line, = plt.plot(x, y, lw=2)
# print(min(y), max(y))
# # Add slider for adjusting the parameter 'a'
# axcolor = 'lightgoldenrodyellow'
# ax_a = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
# slider_a = Slider(ax_a, 'Param a', 0.1, 30.0, valinit=a0)
# # Update the plot with the new value of 'a'
# def update(val):
#     line.set_ydata(f(slider_a.val, x))
#     fig.canvas.draw_idle()
# slider_a.on_changed(update)
# # Add a button for resetting the parameters
# resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
# button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
# def reset(event):
#     slider_a.reset()
# button.on_clicked(reset)
# plt.show()


# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly