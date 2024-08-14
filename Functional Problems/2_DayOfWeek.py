"""
@Author: Samadhan Thube
@Date: 2024-08-13
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-13
@Title: Program to determine the day of the week for a given date
"""

class Util:
    @staticmethod
    def day_of_week(M, D, Y):
        """
        Description:
            Function to determine the day of the week for a given date.
        Parameters:
            M (int): The month of the date (1-12).
            D (int): The day of the date (1-31).
            Y (int): The year of the date.
        Return:
            int: The day of the week as an integer (0=Saturday, 1=Sunday, 2=Monday, ..., 6=Friday).
        """
        y = Y -(14-M)//12
        x = y + (y//4) - (y//100)+(y//400)
        m = (M+12*((14-M)//12)-2)
        d = (D + x + (31*m)//12) % 7

        return d

def main():
    M = int(input("Enter the month (1-12): "))
    D = int(input("Enter the day (1-31): "))
    Y = int(input("Enter the year: "))
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    function = Util.day_of_week(M,D, Y)
    print(f"The day of the week is: {days[function]}")

if __name__ == "__main__":
    main()

