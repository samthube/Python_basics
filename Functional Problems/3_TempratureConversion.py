"""
@Author: Samadhan Thube
@Date: 2024-08-13
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-13
@Title: Program to convert temperatures between Celsius and Fahrenheit
"""

class Util:
    @staticmethod
    def temp_conversion(temp, scale):
        """
        Description:
            Function to convert temperatures between Celsius and Fahrenheit.
        Parameters:
            temp (float): The temperature value to be converted.
            scale (str): The scale of the input temperature ('C' for Celsius or 'F' for Fahrenheit).
        Return:
            float: The converted temperature in the opposite scale.

        """
        if scale.upper() == "F":
            celsius = (temp - 32) * 5/9
            return celsius
        elif scale.upper() == "C":
            fahrenheit = (temp * 9/5) + 32
            return fahrenheit
        else:
            raise ValueError("Enter a proper scale: 'C' for Celsius or 'F' for Fahrenheit")

def main():
    try:
        temp = float(input("Enter the temperature: "))
        scale = input("Enter the scale (C for Celsius, F for Fahrenheit): ")
        converted_temp = Util.temp_conversion(temp, scale)
        if scale.upper() == "F":
            print(f"{temp}°F is {converted_temp:.2f}°C")
        elif scale.upper() == "C":
            print(f"{temp}°C is {converted_temp:.2f}°F")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
