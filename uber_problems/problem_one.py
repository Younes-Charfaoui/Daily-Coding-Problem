""" This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except
the one at i.For example, if our input was [1, 2, 3, 4, 5], the expected output
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
would be [2, 3, 6]. Follow-up: what if you can't use division? """


def get_array_product(array):
    product = 1
    for i in array:
        product *= i
    return product


def get_new_array_division(array):
    new_array = []
    product = get_array_product(array)
    for i in array:
        new_array.append(product/i)
    return new_array

#test
print(get_new_array_division([1,2,3,4,5]))
print(get_new_array_division([3,2,1]))