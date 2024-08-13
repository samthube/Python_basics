'''
@Author: Samadhan Thube
@Date: 2024-08-13 
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-13
@Title : Program to check perfect number
'''

def perfect_num(num):
    """
Description:
    Function used to add divsors of number in the list
Parameter:
      only divisors of given number are added to the list
Return:
      None
"""
    if num <= 0:
        return "Not a valid input for perfect number."
    
    divisors = []
    if(num > 0):
        i =1
        while (i < num):
            remainder = num % i
            if (remainder == 0):
                divisors.append(i)
            i += 1
    total = sum(divisors)
    if total == num:
        print(divisors, "=", num)
        return "Perfect Number"
    else:
        return "Not Perfect Number"


def main():

    num = int(input("Enter the number: "))
    function = perfect_num(num)
    print(function)

if __name__ == "__main__":
    main()