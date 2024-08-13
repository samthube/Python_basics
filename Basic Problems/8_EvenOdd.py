'''
@Author: Samadhan Thube
@Date: 2024-08-12 
@Last Modified by: Samadhan Thube
@Last Modified time:2024-08-12 
@Title :To check weather the number is Even or Odd
'''

def EvenOdd(number):
    """
Description:
    This function used to check that the given number is even or odd
Parameter:
      Used if else block to check the modulo of number with 2
Return:
      The function returns Even if conditon is true and Odd if condition is false 
"""
    
    if (number%2 == 0):
        return "Even"
    else:
        return "odd"

print(EvenOdd.__doc__)    
print(EvenOdd(number = int(input("Enetr the Number:"))))