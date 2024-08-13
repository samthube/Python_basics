'''
@Author: Samadhan Thube
@Date: 2024-08-13 
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-13
@Title : Program to check prime number
'''
def prime_number(num):
    """
    Description:
        Function to check if a given number is prime.
    Parameter:
        num (int): The number to be checked.
    Return:
        None
    """

    count = 2
    while (count < num):
        remainder = num%count
        if (remainder == 0):
           print("Not prime Number ")
           break
        count += 1
    if(remainder != 0):
        print("Prime Number")  

def main():
    num = int(input("Enter the Number:"))
    function = prime_number(num)

if __name__ == "__main__":
    main()