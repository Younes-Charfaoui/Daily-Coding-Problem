""" This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the
list add up to k. For example, given [10, 15, 3, 7] and k of 17, return true
since 10 + 7 is 17. Bonus: Can you do this in one pass? """


# Function of the main problem
def numbers_add_up_to_k(array, k):
    """ a supplementary array to save the numbers we are looking for ,
    say that k is 17 and we current number in the array is 15, this one need 2
    to add up to 17, so we save 2 in our supplementary array and we check if the
    array containing 2 as we move in the array."""
    supp = []

    # simple loop to get all the number in the array.
    for n in array:
        # check if the number is in the supplementary array.
        if is_number_in(supp, n):
            return True
        else:
            # otherwise we calculate the number we need and append it.
            supp.append(k - n)

    return False


# This function search a number in an array and return true if the number is in.
def is_number_in(array, number):
    """
    Check if an array is in numpy array.

    Args:
        array: (array): write your description
        number: (int): write your description
    """
    for n in array:
        if n == number:
            return True
    return False


# print out the result
print(numbers_add_up_to_k([10, 15, 3, 7], 17))
