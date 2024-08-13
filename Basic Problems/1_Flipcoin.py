'''
@Author: Samadhan Thube
@Date: 2024-08-12 
@Last Modified by: Samadhan Thube
@Last Modified time:2024-08-12 
@Title :Flip Coin and print percentage of Heads and Tails
'''
import random

def flip_coin(num):
    """
Description:
    This function used to find percentage of head and tail
Parameter:
      only positive input can be work
Return:
      None
"""
    heads = 0
    tails = 0

    for value in range(num):
        result = random.choice([0, 1])
        if result < 0.5:
            tails += 1
        else:
            heads += 1
            

    heads_percentage = (heads / num) * 100
    tails_percentage = (tails / num) * 100

    print(f"Heads: {heads} ({heads_percentage:.2f}%)")
    print(f"Tails: {tails} ({tails_percentage:.2f}%)")

num = int(input("Enter the flip number"))
flip_coin(num)