'''
@Author: Samadhan Thube
@Date: 2024-08-13 
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-13
@Title : Program to print fibonacci series 
'''


def fibonacci(num):
    """
    Description:
        Function to generate and return a Fibonacci series up to the given number.
    Parameter:
        num (int): The upper limit of the Fibonacci series.
    Return:
        list: The Fibonacci series up to the given number.
    """
    fibonacciList = [0,1]
    num1 = 0
    num2 = 1
    num3 = 0
    while (num3 < num):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        fibonacciList.append(num3)      
    return fibonacciList

def main():

    num = int ( input("Enter the Number upto which Series to be printed : "))
    print(fibonacci(num))

if __name__ == "__main__" :
    main()