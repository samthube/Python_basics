'''
@Author: Samadhan Thube
@Date: 2024-08-12 
@Last Modified by: Samadhan Thube
@Last Modified time:2024-08-12 
@Title :To check weather the number is Even or Odd
'''
def vowel_Consonant():
    """
Description:
    This function used to check the character is vowel or consonant
Parameter:
      The given will be compared with all characters and accordingly print statements work
Return:
      None
"""
vowel = ("a","e","i","o","u")
consonant = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
char = input("Enter the Char: ")
for letter in vowel:
    if (char == letter):
        print("vowel") 
for letter in consonant:
    if (char == letter):
        print("consonant")
    
# print(vowel_Consonant.__doc__)
vowel_Consonant()