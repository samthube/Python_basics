"""
@Author: Samadhan Thube
@Date: 2024-08-13
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-13
@Title: Program to calculate minimum number of notes for a given amount
"""

def vending_machine(num):
    """
    Description:
        Function to generate and return the minimum number of notes needed to make up the given amount.
    Parameter:
        num (int): The amount of money to be made with the available notes.
    Return:
        list: The list of notes used to make up the given amount.
    """
    notes = [1000, 500, 100, 50, 10, 5, 2, 1]
    machine = []

    for note in notes:
        while note <= num:
            machine.append(note)
            num -= note

    print("Number of notes:", len(machine))
    print("Notes:")
    return machine

def main():
    num = int(input("Enter the amount: "))
    notes_list = vending_machine(num)
    print(notes_list)

if __name__ == "__main__":
    main()
