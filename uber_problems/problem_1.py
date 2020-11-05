""" This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except
the one at i.For example, if our input was [1, 2, 3, 4, 5], the expected output
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
would be [2, 3, 6]. Follow-up: what if you can't use division? """


# function to get the product of elements inside an array.
def get_array_product(array):
    """
    Get product : class : class : numpy. product.

    Args:
        array: (array): write your description
    """
    product = 1
    for i in array:
        product *= i
    return product


# this function does the main job of the problem but with division.
def get_new_array_division(array):
    """
    Returns a new array with the same length as the new array

    Args:
        array: (array): write your description
    """
    # array holding the final result
    new_array = []
    # getting the product of the array elements.
    product = get_array_product(array)

    for i in array:
        # for each number divide the product by the current element.
        new_array.append(product / i)

    # return the array
    return new_array


# this function does the main job of the problem without division.(a to -1 power)
def get_new_array(array):
    """
    Return a new array with the new product.

    Args:
        array: (array): write your description
    """
    # array holding the final result
    new_array = []
    # getting the product of the array elements.
    product = get_array_product(array)

    for i in array:
        # for each number product the product by the current element.
        new_array.append(product * (i ** -1))

    # return the array
    return new_array


# This function does the main job of the problem without division.(a to -1 power)
def get_new_array_hard(array):
    """
    Return a new array with new arrays.

    Args:
        array: (array): write your description
    """
    # array holding the final result
    new_array = []

    for i in range(len(array)):
        p = 1
        for j in range(len(array)):
            if j != i:
                p *= array[j]
        new_array.append(p)

    # return the array
    return new_array


# test the functions.
# print(get_new_array_division([1, 2, 3, 4, 5]))
# print(get_new_array_division([3, 2, 1]))
# print(get_new_array([1, 2, 3, 4, 5]))
# print(get_new_array([3, 2, 1]))
print(get_new_array_hard([1, 2, 3, 4, 5]))
print(get_new_array_hard([3, 2, 1]))
