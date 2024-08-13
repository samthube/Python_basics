'''
@Author: Samadhan Thube
@Date: 2024-08-12 
@Last Modified by: Samadhan Thube
@Last Modified time:2024-08-12 
@Title :To find largest number among 3
'''
def largest(num1 , num2, num3):
    """
Description:
    This function used to find the largest number
Parameter:
      If two numbers are same and greater then it will show those two numbers are greater
Return:
      The function returns the statement of greater number according to condition 
"""
    if(num1 >= num2 and num1 >= num3):
        if(num1 == num2 and num1 == num3):
            return "All are same"
        elif(num1 == num3):
            return "Num1 and Num2 is Greater"
        elif(num1 == num2) :
            return "Num1 and Num2 is Greater"
        else:
            return "Num1 is Greater"
    
    elif(num2 > num1 and num2 >= num3):
        if(num2 == num3) :
            return "Num3 and Num2 is Greater"
        else:
            return "Num2 is Greater"
        
    else:
        return "Num 3 is Greater"
    
print(largest.__doc__)
num1 =int(input())
num2 =int(input())
num3 =int(input())
print(largest(num1, num2 ,num3 ))

        