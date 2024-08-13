'''
@Author: Samadhan Thube
@Date: 2024-08-12 
@Last Modified by: Samadhan Thube
@Last Modified time:2024-08-12 
@Title :Program to swap two numbers
'''
def Swap(num1 , num2):
    """
Description:
    This function used to swap two numbers
Parameter:
      only two numbers can be swapped using this function
Return:
      swapped numbers
"""
    temp = num1
    num1 = num2
    num2 = temp
    print("Numbers after swaping")
    return num1 , num2
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(Swap(num1 , num2))