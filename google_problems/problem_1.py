""" This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the
list add up to k. For example, given [10, 15, 3, 7] and k of 17, return true
since 10 + 7 is 17. Bonus: Can you do this in one pass? """

# BRUT FORCE SOLUTION
#
# arr = [10, 15, 3, 7]
# for i in arr:
#     for j in arr:
#         if i + j == 17:
#             print(True)

# ONE PASS SOLUTION
def check(arr, num):
    for i in arr:
        needed_num = num - i
        if needed_num in arr:
            return True

if __name__ == '__main__':
    arr = [10, 15, 3, 7]
    checked = check(arr,17)
    print(checked)