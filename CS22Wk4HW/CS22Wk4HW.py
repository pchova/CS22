####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 4 HW
# Due Date: October 19 2025 
####################################################
import random
import time
import timeit

# Function set_list1D() accepts a 1D array as a parameter
# it replaces each item in the array with a random number between 1-500
def set_list1D(list):
    for item in range(0, len(list)):
        list[item] = random.randint(0,500)
    return list

# Function show_list1D() prints a 1D array on a single line
def show_list1D(list):
    for item in range(0, len(list)):
        print(list[item], end=' ')
    print()

def set_list2D(list):
    for x in range(0, len(list)):
        for y in range(0, len(list)):
            list[x][y] = random.randint(0,500)
    return list

def show_list2D(list):
    for x in range(0, len(list)):
        for y in range(0, len(list)):
            print(list[x][y], end= ' ')
        print()
    print()

def main():
    #create a 1 dimensional array with 10 elements
    #list1 = [0] * 10
    #print(list1)
    #set_list1D(list1)
    #show_list1D(list1)

    #print()

    #create a 2 dimensional array with 10 rows and 10 columns
    #list2 = [[0] * 10] * 10 - this is wrong! this creates a shallow copy!
    #list2 = [[0] * 10 for i in range(10)]
    #print(list2)
    #set_list2D(list2)
    #show_list2D(list2)

    list1 = [0] * 10
    list2 = [[0] * 10 for i in range(10)]

    start_time = time.perf_counter()
    set_list1D(list1)
    total_time = time.perf_counter() - start_time
    print(f"set_list1D took {total_time} seconds to execute.")
    

main()
