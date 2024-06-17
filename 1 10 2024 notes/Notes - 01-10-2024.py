#####################
## Dalton Murray    #
## 01/08/2024       #
## Notes            #
#####################
import sys # Required for system variables

# Defines the __main__ function
def __main__():
    # print(5 * "Hello World!")

    # string1 = "Lel"
    # string2 = 5 * string1

    # print(string2)

    # string1 = string1 * 5
    # print(string1)

    # num1 = 5
    # print("The number is", num1)
    # print(f"The number is {num1}")

    # numFloat = 5.46
    # print(type(numFloat))
    # print(numFloat)

    # name = "Dalton"
    # print(type(name))
    # print(f"The name of my student is {name}")

    # is_student = True # False
    # print(type(is_student))
    # print(is_student)

    inputName = input("What is your name? ")
    print("Hello, ", inputName)

    inputYearBirth = int(input("What is your year of birth? "))
    age = 2024 - inputYearBirth
    print(inputName, "is", age, "years old")

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly