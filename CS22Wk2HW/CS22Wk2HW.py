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

main()