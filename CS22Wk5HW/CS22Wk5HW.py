####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 5 HW
# Due Date: October 26 2025 
####################################################

def main():
    input1 = int(input('Enter a number greater than 0: '))
    input2 = int(input('Enter a second number greater than 0: '))
    print(input1, "*", input2,"=",rec_mult(input1, input2))

    print()

    numbers = int(input("Enter a number greater than 0: "))
    print("The sume of the numbers from 1 to", numbers, "is", rec_sum(numbers))

    print()

    my_list = [4, 13, 20, 18, 26, 28, 33, 44]
    print("The sum of the elements of",my_list,"is",rec_list_sum(my_list))

# Function rec_list_sum() accepts a list parameter to recursively add
# each item in the list and return its sum
def rec_list_sum(list):
    #base case - when list ends return 0 
    if not list:
        return 0
    else:
        return list[0] + rec_list_sum(list[1:])

# Function rec_sum() accepts 1 integer parameter to recursively add the sum
# of all integers to the parameter (inclusive)
def rec_sum(n):
    #base case, once n equals zero return 0
    if n == 0:
        return 0
    else:
        #add n + (n-1) till n = 0
        return n + rec_sum(n-1)

# Function rec_mult() accepts two integer parameters to recursively find the
# multiplication sum. Achieved by repeated addition of the int 'y'... 'x' amount of times
def rec_mult(x, y):
    #base case - if x equals 1 then just add one more increment of y to sum
    if x == 1:
        return y
    else:
        # y + 'x times of the amount of y' until we hit the base case
        return y + rec_mult(x-1, y)

main()
