#####################
## Dalton Murray    #
## 01/22/2024       #
## Notes            #
#####################
import sys # Required for system functions

# Defines the __main__ function
def __main__():

    # Tuples
    coordinateNY = (40.71, -74.006) # Tuple's are immutable, cannot modify once set
    print(coordinateNY[0])

    books = ("Python 101", "Data Science", "Machine Learning")
    print(books[0:])
    print(books[1:])

    newBooks = ("Data Mining for Business", "Texting")

    books = books + newBooks # Concatenate tuples
    print(books)

    allBooks = books * 2
    print(allBooks)

    for item in books: # Can set item/i to anything
        print(item)

    studentInfo = ("Alice", "A001", "Computer Science")
    name, id, major = studentInfo
    print(type(studentInfo))
    print(type(name))
    print(name, id, major)

    studentName, *etc = studentInfo # In name if uninterested in rest of items can do *
    print(studentName)
    print(*etc)


    values = [3, 4, 5, 7]
    print(max_min(values))

    # # Dictionaries
    # aliceInfo = {"name":"Alice", "id":"A001", "major":"Computer Science", "age":25, "courses":{}}
    # bobInfo = {"name":"Bob", "id":"A003", "major":"Business", "age":26}
    # studentsInfo = {"1": aliceInfo, "2":bobInfo}

    # aliceInfo["sex"] = "Female"
    # print(aliceInfo)
    # print(aliceInfo["name"])

    # aliceInfo["major"] = "Business"
    # print(aliceInfo)

    # print(studentsInfo)

    # print(studentsInfo["2"]["name"])

    # # Sets
    # stock = {"P001", "P002", "P003"}
    # print(type(stock))

    # print(stock)
    # stock.add("P002")
    # print(stock)
    # stock.add("P004")
    # print(stock)

    # clientsEvents1 = {"Alice", "Bob", "Charlie"}
    # clientsEvents2 = {"Bob", "Diana", "Edward"}
    # print(clientsEvents1.union(clientsEvents2))
    # print(clientsEvents1.intersection(clientsEvents2))

    # if "Jessica" in clientsEvents2:
    #     print("Yes")
    # else:
    #     print("No")

    # print(len(clientsEvents1.intersection(clientsEvents2)))
    # print(len(clientsEvents2))


def max_min(nums):
    return min(nums), max(nums)

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly