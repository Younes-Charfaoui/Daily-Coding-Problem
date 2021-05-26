"""This problem was asked by Google.

Given an array of integers where every integer occurs three times except
for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], 
return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space."""

# FIsrt try
arr = [6, 1, 3, 3, 3, 6, 6]
def get_duplicated(arr=arr):
    dic = []
    for i in arr:
        if i in dic:
            dic.remove(i)
        else:
            dic.append(i)
    return dic

arr = get_duplicated()
print(arr)