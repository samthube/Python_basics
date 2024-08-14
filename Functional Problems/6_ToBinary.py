'''
@Author: Samadhan Thube
@Date: 2024-08-14
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-14
@Title: Binary Conversion and Representation
'''

def to_binary(num):
    """
    Converts a decimal number to its 32-bit binary representation.

    Description:
        This function takes an integer and converts it to a binary string. 
        It performs the conversion by repeatedly dividing the number by 2 and 
        collecting the remainders. The binary digits are then reversed and 
        zero-padded to ensure a 32-bit representation.

    Parameter:
        num (int): The decimal number to be converted to binary.

    Return:
        str: The 32-bit binary representation of the input number as a string.
    """
    binary_list = []
    while num > 0:
        remainder = num % 2
        binary_list.append(str(remainder))
        num = num // 2
    binary_list.reverse()
    binary_string = ''.join(binary_list).zfill(32)  
    return binary_string

def main():
    num = int(input("Enter the decimal number: "))
    binary_representation = to_binary(num)
    print(f"The binary representation of {num} is {binary_representation}")

if __name__ == "__main__":
    main()