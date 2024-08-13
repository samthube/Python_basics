'''
@Author: Samadhan Thube
@Date: 2024-08-12 
@Last Modified by: Samadhan Thube
@Last Modified time:2024-08-12 
@Title :Program to Compute Quotient and Remainder
'''
def quotient(divident , divider):
    """
Description:
    This function used to find the quotient of given numbers
Parameter:
      The given two numbers are get divided and quotient get calculated
Return:
      The function returns quotient
"""
    quotient = divident/divider
    print("Quotient is : ")
    return quotient

def remainder(divident ,divider):
    """
Description:
    This function used to find the remainder of given numbers
Parameter:
      The given two numbers are get divided and remainder get calculated
Return:
      The function returns remainder
"""
    remainder = divident%divider
    print("Remainder is : ")
    return remainder

divident = int(input("Enter divident"))
divider = int(input("Enter divider"))
print(quotient(divident , divider))
print(remainder(divident,divider))