#!/usr/bin/python3

def minOperations(n):
    if (type(n) != int):
        return 0

     if (n < 2):
         return 0

     minOps = 0

     for i in range(2, (n + 1)):
         while (n % i == 0):
             minOps += i
             n //= i

             return minOps
