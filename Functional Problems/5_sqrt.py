"""
@Author: Samadhan Thube
@Date: 2024-08-13
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-13
@Title: Program to compute the square root of a nonnegative number
"""

def sqrt(c):
    """
    Description:
        Function to compute the square root of a nonnegative number using Newton's method.
    Parameters:
        c (float): The nonnegative number for which the square root is to be computed.
    Return:
        float: The computed square root of the number.

    """
    if c < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    epsilon = 1e-15
    t = c  
    
    while abs(t * t - c) > epsilon * t:
        t = (t + c / t) / 2
    
    return t

def main():
    c = int(input("Enter a nonnegative number: "))
    result = sqrt(c)
    print(f"Square root of {c} is {result}")

if __name__ == "__main__":
    main()
