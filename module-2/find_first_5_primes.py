# CSD325: Advanced Python
# Module 12.2: Redo Assignment -
#   Module 2.2 Assignment: Documented Debugging + Flowchart(s)
# Isaac Ellingson
# 12/21/2025

# I did not write this.
# This is an example program from https://pynative.com/python-find-sum-of-first-n-prime-numbers/

import math
import pdb

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):  # optimized by the checking till √n
        if num % i == 0:
            return False
    return True

n = 4   # first 5 prime numbers
prime_sum = 0   # sum of prime numbers
prime_counter = 0 # counter of prime numbers
num = 2  # Start from the first prime number

pdb.set_trace() ######### Breakpoint is here

while prime_counter < n:
    if is_prime(num):
        print(num)
        prime_sum += nums # INTENTIONAL ERROR INTRODUCED: num -> nums
        prime_counter += 1
    num += 1
print(f"The sum of the first {n} prime numbers is: {prime_sum}")
