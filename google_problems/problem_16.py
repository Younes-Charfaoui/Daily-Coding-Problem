"""This problem was asked by Google.
Given a list of integers S and a target number k, write a function
that returns a subset of S that adds up to k. If such a subset cannot
be made, then return null.
Integers can appear more than once in the list. You may assume
all numbers in the list are positive.
For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it
sums up to 24.
"""

# function to filter element smaller than k.
def subset_sum(nums, k):
    if k == 0:
        return []
    if not nums and k != 0:
        return None

    nums_copy = nums[:]
    last = nums_copy.pop()

    with_last = subset_sum(nums_copy, k - last)
    without_last = subset_sum(nums_copy, k)
    if with_last is not None:
        return with_last + [last]
    if without_last is not None:
        return without_last

subset_sum([12, 1, 61, 5, 9, 2] , 24)