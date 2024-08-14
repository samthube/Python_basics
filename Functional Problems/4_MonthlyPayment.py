"""
@Author: Samadhan Thube
@Date: 2024-08-13
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-13
@Title: Program to calculate monthly loan payments
"""
class Util:
    @staticmethod
    def monthly_payment(P, Y, R):
        """
        Description:
            Function to calculate the monthly payment for a loan based on the principal amount,
            number of years, and annual interest rate.
        Parameters:
            P (float): The principal loan amount.
            Y (int): The number of years to pay off the loan.
            R (float): The annual interest rate (as a percentage).
        Return:
            float: The monthly payment amount.
        """
        n = 12 * Y
        r = R / (12 * 100)

        payment = (P * r) / (1 - (1 + r) ** -n)
        return payment

def main():
    P = int(input("Enter the principal loan amount (P): "))
    Y = int(input("Enter the number of years to pay off the loan (Y): "))
    R = int(input("Enter the annual interest rate (R): "))

    function = Util.monthly_payment(P, Y, R)
    print(f"Monthly payment: {function:.2f}")

if __name__ == "__main__":
    main()
