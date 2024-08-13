'''
@Author: Samadhan Thube
@Date: 2024-08-12 
@Last Modified by: Samadhan Thube
@Last Modified time:2024-08-12 
@Title :This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.
'''
def power(N):
    """
Description:
    This function used to calculate power of 2
Parameter:
      The power of 2 will be calculated till the provided number
Return:
      None
"""
    count = 1
    if(N > 0 or N <31):

     while count <= N:
        power = 2**count
        print(2 , "^" , count , "=", power)
        count += 1

    else:
      print("Provide number less than 31 and greater than 0")

power(N = int(input()))