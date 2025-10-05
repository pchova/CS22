####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 2 Homework Assignment
# Due Date: October 5 2025
####################################################
import random

def main():
    #Program 1
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
    print()

    #Program 2
    statecaps = {}

    #open file for reading 
    with open('statecapitals.txt', 'r') as proxy:

        # Populate the dictionary so that each state/capital is a key/value pair
        state = proxy.readline().rstrip("\n")
        capital = proxy.readline().rstrip("\n")

        # while there no lines left, read each line for the state and capital
        # add each pair to statecaps dictionary
        while state != "":
            statecaps[state] = capital
            state = proxy.readline().rstrip("\n")
            capital = proxy.readline().rstrip("\n")

    print(statecaps)

    rightAnswers = 0
    wrongAnswers = 0

    for key in statecaps:
        userInput = input(f"What is the capital of {key}: ")
        if userInput != statecaps[key]:
            print(f"Wrong! The correct answer is {statecaps[key]}")
            wrongAnswers += 1
        elif userInput == statecaps[key]:
            print(f"Right! The answer is {statecaps[key]}")
            rightAnswers += 1

    print(f"You got {rightAnswers} answer(s) right and {wrongAnswers} answer(s) wrong")



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
    
    #return numbers greater than user input or write none
    if not largerNums:
        return f"There are no numbers greater than {num} in the list."
    else:
        return f"Numbers greater than {num}: {formatNums}"
        

main()