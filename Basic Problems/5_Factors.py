'''
@Author: Samadhan Thube
@Date: 2024-08-12 
@Last Modified by: Samadhan Thube
@Last Modified time:2024-08-12 
@Title :Computes the prime factorization of N using brute force.
'''
def prime_factors(num):
    """
Description:
    Finds the prime factorization of a number n
Parameter:
      ..
Return:
      factors
"""  
    factors = []
    i = 2
    while i * i <= num:
      while num % i == 0:
        factors.append(i)
        num //= i
        i += 1
      if num > 1:
       factors.append(num)
       return factors
num = int(input("Enter the number"))
print(prime_factors(num))