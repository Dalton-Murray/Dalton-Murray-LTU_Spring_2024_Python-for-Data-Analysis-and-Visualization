#####################
## Dalton Murray    #
## 01/17/2024       #
## Assignment 1     #
#####################
import sys # Required for system functions

# Defines the __main__ function
def __main__():

    # Get 3 largest numbers of nums, assuming unknown inputs for list
    # Method #1: As shown in-class
    # Base nums from in-class
    nums = [4, 3, 2, 78, 32, 12, 11, 10, 7.8] # Prints 78, 32, 12
    # Validation all negative nums
    # nums = [-0.11, -0.92, -5, -99, -18, -0.32] # Prints -0.11, -0.32, -0.92
    # Validation mixed nums
    # nums = [0, -99, 1, -0.2, -0.32, -8, 2] # Prints 2, 1, 0

    # Set base variables to the index of nums at certain base positions
    maxNum1 = nums[0]
    maxNum2 = nums[1]
    maxNum3 = nums[2]

    for i in range(2, len(nums)):
        if nums[i] > maxNum1:
            maxNum3 = maxNum2 # Add this line ensuring maxNum3 is also set to maxNum2 if i is greater than maxNum1
            maxNum2 = maxNum1
            maxNum1 = nums[i]
        elif nums[i] > maxNum2:
            maxNum3 = maxNum2 # Ensuring that if the current increment/index is higher than maxNum2 to also set maxNum3 to the previous maxNum2
            maxNum2 = nums[i]
        elif nums[i] > maxNum3:
            maxNum3 = nums[i] # Ensuring that if the current index is greater than maxNum3 that I set maxNum3 to it

    print("Max num 1: \n", maxNum1, "\nMax num 2: \n", maxNum2, "\nMax num 3: \n", maxNum3)

    # Method #2: An easier way using sorted there are also easier ways to do this too
    # Base nums from in-class
    nums = [4, 3, 2, 78, 32, 12, 11, 10, 7.8] # Prints [78, 32, 12]
    # Validation all negative nums
    # nums = [-0.11, -0.92, -5, -99, -18, -0.32] # Prints [-0.11, -0.32, -0.92]
    # Validation mixed nums
    # nums = [0, -99, 1, -0.2, -0.32, -8, 2] # Prints [2, 1, 0]
    top3Nums = sorted((nums), reverse = True)[:3] # Sort typically sorts by lowest - highest, this reverses that so the first 3 are the highest, then cut the first 3 rather than having to get the length of the list
    # This is also easier than having to continue adding to the previous if and elif's from in-class as I can simply change the number and get how many I want
    # Since it's a list I could easily splice it and output the 3 index's separately but instead I will just print it out
    print(top3Nums)


    # Used to separate the previous task and new task if running everything at the same time and not commented out
    print("\n")


    # Get moving average of nums index 0 1 2, 1 2 3, 2 3 4, 5 6 7, etc.
    # My interpretation of what was asked in class was for us to keep track of the averages of blocks of 3 index's/numbers, however, I am unsure if exactly we were supposed to do blocks of 3 so I made it easily configurable
    # Base nums from in-class
    nums = [4, 3, 2, 78, 32, 12, 11, 10, 7.8] # Prints [3.0, 27.67, 37.33, 40.67, 18.33, 11.0, 9.6]
    # Validation all negative nums
    # nums = [-0.11, -0.92, -5, -99, -18, -0.32] # Prints [-2.01, -34.97, -40.67, -39.11]
    # Validation mixed nums
    # nums = [0, -99, 1, -0.2, -0.32, -8, 2] # Prints [-32.67, -32.73, 0.16, -2.84, -2.11]
    block = 3
    movAverage = []
    i = 0

    while i < len(nums) - block + 1: # The condition for the while loop is if the increment is less than than length of numbers minus the block/3 + 1 to account for indexing starting at 0
        # print(nums[i:i + block])
        currentBlock = nums[i:i + block] # What this is doing is setting the current increment of the loop to the index of nums then adding 3
        # print("The current block of numbers are:", currentBlock)
        currentAverage = round(sum(currentBlock) / block, 2) # What this does is takes the current block of numbers, then sums it (adds them up) then divide it by block which is 3/the amount of numbers in the list, then rounds to 2 decimals
        # This will output [3.0, 27.666666666666668, 37.333333333333336, 40.666666666666664, 18.333333333333332, 11.0, 9.6] if I don't round it, so to make it more neat I round it to 2 decimals
        # print("The current average for this block is:", currentAverage)

        movAverage.append(currentAverage)
        # Increments i until it meets the condition of the while loop
        i += 1
    print("\nThe moving average is:\n", movAverage)
    # This is a list of the sum of each block of 3
    # To confirm this, I put into a calculator 4 + 3 + 2 = 9 then divide by 3 = 3, I can just take any consecutive set of 3 numbers add it then divide by 3 to confirm that it is correct
    # I can then easily splice this array and print out each of the averages of the blocks of 3, or I can add into the loop to output the 3 numbers then output the average, however, my understanding is that this isn't what is being asked for but I included it as comments anyways


# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly