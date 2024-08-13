'''
@Author: Samadhan Thube
@Date: 2024-08-13 
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-13
@Title : Program to check prime number
'''
def prime_number(num):

    count = 2
    while (count < num):
        remainder = num%count
        if (remainder == 0):
           print("Not prime Number ")
           break
        count += 1
    if(remainder != 0):
        print("Prime Number")  

num = int(input("Enter the Number:"))
prime_number(num)