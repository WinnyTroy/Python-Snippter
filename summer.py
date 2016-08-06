#!/usr/bin/env python

# create variable to hold total
# if num % 2 == 0
# divide it by  2
# elif num % 2 != 2
# num * 2

# """
# Create a function that:
# 1. Halves even numbers
# 2. Doubles odd numbers
# 3. Returns the sum of all
# """


# l = [45, 90, 85, 60]
total = 0
even = 0
odd = 0


def super_sum(list):
# use of a global keyword to use local variable.
# local variables are instantiated within the function.
    global even
    global odd
    global total
    for l in list:
        if l % 2 == 0:
            even += l / 2
        elif l % 2 != 0:
            odd += l * 2
    total = even + odd
    return total


# total = even + odd

print super_sum([45, 90, 85, 60])
