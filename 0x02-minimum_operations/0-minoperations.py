#!/usr/bin/python3

def minOperations(n):
    if n <= 0:
        return 0

    operations = 0
    clipboard = 0
    H_chars = 1


    while H_chars < n:
        if n % H_chars == 0:
            clipboard = H_chars
            operations += n // H_chars - 1

        else:
            operations += 1

            H_chars += clipboard

            return operations if H_chars == n else 0
