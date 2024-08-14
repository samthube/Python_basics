'''
@Author: Samadhan Thube
@Date: 2024-08-13 
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-13
@Title : Program to reverse the number
'''
def reverse_number(num):
    """
    Description:
        Function to reverse the digits of a given number.
    Parameter:
        num (int): The number to be reversed.
    Return:
        int: The number obtained by reversing the digits of the input number.
    """
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return reverse

def main():
    num = int(input("Enter the number: "))
    r = reverse_number(num)
    print(f"Reverse: {r}")

if __name__ == "__main__":
    main()
