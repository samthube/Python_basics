'''
@Author: Samadhan Thube
@Date: 2024-08-12 
@Last Modified by: Samadhan Thube
@Last Modified time:2024-08-12 
@Title :Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
'''
def harmonic(N):
    if(N != 0):
        count = 1
        j = 0
        while (count <= N):
            harmonic = 1/count + j
            j = harmonic
            count +=1
    print("Harmonic value is : ",j)
N=int(input())
harmonic(N)