'''
@Author: Samadhan Thube
@Date: 2024-08-14
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-14
@Title: Binary Conversion and Representation
'''
def to_binary(num):
    binary_represnt = bin(num)[2:]
    return binary_represnt
print(to_binary(100))