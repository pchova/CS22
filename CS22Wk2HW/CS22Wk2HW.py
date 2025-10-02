####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 2 Homework Assignment
# Due Date: October 5 2025
####################################################
import random

def main():
    #declare an array with 5 elements
    nums_list = [0] * 5

    #assign a random value between 1-100 to each element in array
    for i in range(len(nums_list)):
        randNumber = random.randint(1,100)
        nums_list[i] = randNumber

    #take user input and convert it to int variable
    the_num = int(input("Enter an integer: "))
    #print(type(the_num))

    print("Here is your list: ", nums_list)
    print(bigsmall(the_num, nums_list))

def bigsmall(num, list):
    i = 0
    largerNums = []

    #while count is less than length of the list, go through to find num > user input
    while i < len(list):
        if list[i] > num:
            largerNums.append(list[i])
        i += 1
    
    #convert largerNums list to str and join them with a single space
    formatNums = " ".join(str(num) for num in largerNums)
    
    #return numbers greater than user input
    return f"Numbers greater than {num}: {formatNums}"
        

main()