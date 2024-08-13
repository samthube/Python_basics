'''
@Author: Samadhan Thube
@Date: 2024-08-13 
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-13
@Title : Program to check perfect number
'''
divisors = []
def perfect_num(num):
    if(num > 0):
        i =1
        while (i < num):
            remainder = num % i
            if (remainder == 0):
                divisors.append(i)
            i += 1
    

def add():
    temp = 0
    for val in divisors:
        sum = val + temp
        temp = sum
    if (temp == num):
        print(divisors ,"=" , num)
        return "Perfect Number"
    else:
        return "Not Perfect Number"

num = int(input("Enter the number: "))
perfect_num(num)
print(add())
