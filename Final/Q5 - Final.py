#####################
## Dalton Murray    #
## 04/29/2024       #
## Q5               #
#####################
import sys

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def __main__():

    # Defines the Book class
    class Book:
        def __init__(self, title, author, isbn):
            # Initalizes title, author, and isbn
            self.title = title
            self.author = author
            self.isbn = isbn

        def description(self):
            # Returns: str: A formatted string with book details.
            return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    # Create an object of the Book class with specified title, author, and ISBN.
    book1 = Book("1984", "George Orwell", "978-0451524935")

    # Call the description method on the book1 object and print the result.
    print(book1.description())

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly
