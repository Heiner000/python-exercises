# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a function,
# need a return statement, need a for loop to iterate over the array.
#
# Example function call:
#
# multiply_by([1, 2, 3], 5)
#
# [5, 10, 15]
#
# Write a function called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.

list = [1,2,3]

def multiply_by(arr, num):
    product = []
    for i in arr:
        product.append(i * num)
    return product

print(multiply_by(list, 5))