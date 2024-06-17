#####################
## Dalton Murray    #
## 04/01/2024       #
## Notes            #
#####################
import sys # Required for system functions

import pandas as pd # Imports the pandas library and sets an alias to pa
import numpy as np # Imports the numpy library and sets an alias to np
import matplotlib.pyplot as plt # Imports matplotlib pyplot library and sets an alias to plt
import seaborn as sns # Imports seaborn and sets an alias to sns

# Defines the __main__ function
def __main__():

    # Object Oriented Profgramming (OOP)
    def calculate_area(length, width):
        # area = length * width
        return length * width
    def calculate_perimeter(length, width):
        # perimeter = 2 * (length + width)
        return 2 * (length + width)

    l = 5
    w = 3
    area = calculate_area(l, w)
    perimeter = calculate_perimeter(l, w)
    print(area, perimeter)

    class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def calculate_area(self):
            return self.length * self.width

        def calculate_perimeter(self):
            return 2 * (self.length + self.width)

    rect = Rectangle(3, 5)
    print(rect.calculate_perimeter())
    print(rect.calculate_area())

    class Student_py:
        class_name = "Python for Data Visualization and Analysis"

        def __init__(self, name, student_ID, assign, attendance, work_status):
            self.name = name
            self.student_ID = student_ID
            self.assign = assign
            self.attendance = attendance
            self.work_status = work_status

        def working(self):
            if self.work_status == 0:
                print(f"{self.name} is not working")
            else:
                print(f"{self.name} is working")

        def ID(self):
            print(self.student_ID)

    ali = Student_py("Alice", 343, 2, 9, 0)
    bob = Student_py("Robert", 344, 3, 11, 1)
    ali.working()
    ali.ID()
    print(ali.class_name)
    print(bob.class_name)

    class Rectangle():
        def __init__(self, length, width, x_o, y_o):
            self.length = length
            self.width = width
            self.x_o = x_o
            self.y_o = y_o

        def xRange(self):
            x_low = self.x_o - self.length / 2
            x_high = self.x_o + self.length / 2
            print(f"The Rectangle is between {x_low} and {x_high} on the X-Axis")

        def yRange(self):
            y_low = self.y_o - self.width / 2
            y_high = self.y_o + self.width / 2
            print(f"The Rectangle is between {y_low} and {y_high} on the Y-Axis")

    rect = Rectangle(4, 2, 0, 0)
    rect.xRange()
    rect.yRange()

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
