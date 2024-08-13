'''
@Author: Samadhan Thube
@Date: 2024-08-12 
@Last Modified by: Samadhan Thube
@Last Modified time:2024-08-12 
@Title :To check weather the year is leap or not
'''
def leap_year(year):
    """
Description:
    This function used to check if year is leap or not
Parameter:
      If regular years are divisible by 4 then the year is leap 
      If centurial years divisible by 400 then also they are leap
Return:
      The function returns weather the year is leap or not
"""
    if (year < 1000 or year > 9999):
        return "Enter proper format" 
    if(year%4 == 0):
        return "Leap year"
    elif(year%400 == 0):
        return "Leap year"
    else:
        return "Not Leap year"
    
print(leap_year.__doc__)
print(leap_year(year= int(input("Enter the Year(YYYY):"))))