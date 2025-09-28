####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 1 - Python Primer Part 1
# Due Date: September 28, 2025
####################################################
import random

def main():
    #open a file for writing
    nums = open('numbers2.txt', 'w')

    #use for loop and randint method to write 10 nums to the file
    for i in range(10):
        n = random.randint(1,1000)
        nums.write(str(n) + '\n')

    #close file
    nums.close()

    #open file again, but for reading
    nums = open('numbers2.txt', 'r')

    #call evensodds, pass nums as parameter
    print(evensodds(nums))
    nums.close()
    

# Function evensodd() accepts a file parameter and reads each number in the file
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
        else:
            #else print msg that number count not be read
            print("number could not be read.")

        #read next line in the file
        line = file.readline()
    
    #return oddCount and evenCount
    return f"There are {evenCount} even numbers and {oddCount} odd numbers in the file."
    

main()


