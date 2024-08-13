'''
@Author: Samadhan Thube
@Date: 2024-08-13 
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-13
@Title : Program to print fibonacci series 
'''
fibonacciList = [0,1]

def fibonacci(num):
    """
Description:
    Function used to print fibonacci series
Parameter:
      Series will be printed till given number
Return:
      Fibonacci series
"""

    num1 = 0
    num2 = 1
    num3 = 0
    while (num3 < num):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        fibonacciList.append(num3)      
    return fibonacciList

num = int ( input("Enter the Number upto which Series to be printed : "))
print(fibonacci(num))