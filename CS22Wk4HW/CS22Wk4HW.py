####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 4 HW
# Due Date: October 19 2025 
####################################################
import random
import time
import timeit

def main():
    #create a 1 dimensional array with 10 elements
    list1 = [0] * 10
    print(list1)

    #create a 2 dimensional array with 10 rows and 10 columns
    #list2 = [[0] * 10] * 10 - this is wrong! this creates a shallow copy!
    list2 = [[0]*10 for i in range(10)]
    print(list2)

main()
