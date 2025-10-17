####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 4 HW
# Due Date: October 19 2025 
####################################################
import random
import time
import timeit

# Function set_list1D() accepts a list as a parameter
# it replaces each item in the list with a random number between 1-500
def set_list1D(list):
    for item in range(0, len(list)):
        list[item] = random.randint(0,500)
    return list


def main():
    #create a 1 dimensional array with 10 elements
    list1 = [0] * 10
    print(list1)
    print(set_list1D(list1))

    #create a 2 dimensional array with 10 rows and 10 columns
    #list2 = [[0] * 10] * 10 - this is wrong! this creates a shallow copy!
    #list2 = [[0] * 10 for i in range(10)]
    #print(list2)

main()
