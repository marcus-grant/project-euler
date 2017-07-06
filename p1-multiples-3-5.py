# Project Euler Problem 1
# Multiples of 3 & 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, -
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# import numpy to speed this problem up significantly
import numpy as np

# start by creating a sieve for all multiples of 3 & 5
# sieves are WAAAAY faster than modulo's, but they do take up more memory
max = 999
sieve = np.zeros(max + 1, dtype=bool)

# check that the sieve is proper
# NOTE that the sieve only needs to start at 3 and include only odd numbers
print(repr(sieve))

# go through each index, which represents a # from 0 to max in 3 increments
current_number = 3
while current_number <= max:
    sieve[current_number] = True
    current_number += 3

# do the same for increments of 5
current_number = 5
while current_number <= max:
    sieve[current_number] = True
    current_number += 5

# now again, using the index as the number of the sieve, add up the total
multiples_sum = 0
current_number = 3
while current_number <= max:
    if sieve[current_number]:
        multiples_sum += current_number
    current_number += 1

message = "The sum of all multiples of 3 & 5 from 3 to " + str(max)
message += ", exclusively, is: " + str(multiples_sum)
print(message)
