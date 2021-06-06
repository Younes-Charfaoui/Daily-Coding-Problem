"""This problem was asked by Google.

Given an array of integers where every integer occurs three times except
for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], 
return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space."""


arr = [6, 1, 3, 3, 3, 6, 6]
def get_unique(arr=arr):
    for num in arr:
        i = arr.index(num)
        if num in arr[0:i] or num in arr[i+1::]:
            continue
        else:
            return num

arr = get_unique()
print(arr)
arr = get_unique([13, 19, 13, 13])
print(arr)