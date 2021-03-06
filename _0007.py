#!/usr/bin/env python3
# cython: language_level=3
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
from libs import primes
primegen = primes.prime(100000000)
lastnum = next(primegen)
for i in range(10000):
    lastnum = next(primegen)
print(lastnum)
