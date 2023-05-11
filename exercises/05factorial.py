# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120
#
# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(factorial(5))