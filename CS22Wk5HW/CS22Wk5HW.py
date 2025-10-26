####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 5 HW
# Due Date: October 26 2025 
####################################################

def main():
    input1 = int(input('Enter a number greater than 0: '))
    input2 = int(input('Enter a second number greater than 0: '))

    print(input1, " * ", input2," = ",rec_mult(input1, input2))

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
