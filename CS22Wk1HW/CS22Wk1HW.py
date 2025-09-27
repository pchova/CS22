####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 1 - Python Primer Part 1
# Due Date: September 28, 2025
####################################################
import random

def main():
    #open a file numbers.txt for writing
    #open file to be able to write to file
    nums = open('numbers2.txt', 'w')

    #use a for loop and randint method to write
    #10 numbers to the file , between 1-1000
    #each num converted to a str, and have \n added to it
    for i in range(10):
        n = random.randint(1,1000)
        nums.write(str(n) + '\n')

    nums.close()

    with open('numbers3.txt', 'w') as nums:
        for i in range(10):
            nums.write(str(random.randint(1,1000)) + '\n')

    #open file again, but for reading
    nums = open('numbers2.txt', 'r')
    print(evensodds(nums))
    nums.close()
    

#create a function evensodds with 1 parameter for file
def evensodds(file):
    oddCount = 0
    evenCount = 0

    while file.readline() != "":
        for n in file:
            num = int(n.rstrip('\n'))

            if num % 2 == 0:
                evenCount += 1
            elif num % 2 != 0:
                oddCount += 1
            else:
                print("number could not be read.")
        
        return f"There are {evenCount} even numbers and {oddCount} odd numbers in the file."


main()