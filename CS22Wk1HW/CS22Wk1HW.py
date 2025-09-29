####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 1 - Python Primer Part 1
# Due Date: September 28, 2025
####################################################
import random

def main():
    #open a file for writing
    nums = open('numbers.txt', 'w')

    #use for loop and randint method to write 10 nums to the file
    for i in range(10):
        n = random.randint(1,1000)
        nums.write(str(n) + '\n')

    nums.close()

    #open file again, but for reading
    nums = open('numbers.txt', 'r')

    #call evensodds(), pass nums as parameter
    print(evensodds(nums))
    nums.close()

    #open 'steps.txt' file for reading, call get_steps() for each month
    with open('steps.txt', 'r') as steps:
        get_steps('January', 31, steps)
        get_steps('February', 28, steps)
        get_steps('March', 31, steps)
        get_steps('April', 30, steps)
        get_steps('May', 31, steps)
        get_steps('June', 30, steps)
        get_steps('July', 31, steps)
        get_steps('August', 31, steps)
        get_steps('September', 30, steps)
        get_steps('October', 31, steps)
        get_steps('November', 30, steps)
        get_steps('December', 31, steps)


# Function get_steps() accepts a string for month, 
# int for days in the month, and a file object
# Prints statement with average num of steps per month
def get_steps(month, days, file):
    total = 0

    #read number of steps for each day of the month
    for i in range(days):
        line = file.readline()
        steps = int(line.rstrip('\n'))
        total += steps

    #calculate avg number of steps in the month
    avgNum = total // days

    #print the month and average number of steps
    print(f"User walked an average of {avgNum} steps in {month}")


# Function evensodds() accepts a file parameter and reads each number in the file
# Returns a string with how many even and odd numbers found
def evensodds(file):
    oddCount = 0
    evenCount = 0

    #read first line of the file
    line = file.readline()

    #while first line of file is not empty, read the string, strip the newline and convert to int
    while line != "":
        num = int(line.rstrip('\n'))

        #if number is even or odd
        if num % 2 == 0:
            evenCount += 1
        elif num % 2 != 0:
            oddCount += 1

        #read next line in the file
        line = file.readline()
    
    #return oddCount and evenCount
    return f"There are {evenCount} even numbers and {oddCount} odd numbers in the file."
    

main()


