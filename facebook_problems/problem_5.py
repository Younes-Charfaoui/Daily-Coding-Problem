"""This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
"""
import math


# code each character with a number
def code(i):
    if i == "(":
        return 1
    elif i == ")":
        return -1
    elif i == "[":
        return 2
    elif i == "]":
        return -2
    elif i == "{":
        return 3
    elif i == "}":
        return -3


# main function of the problem
def validate(arr):
    new_array = []
    for i in arr:
        new_array.append(code(i))
    val_arr = []
    for i in new_array:
        if len(val_arr) == 0:
            val_arr.append(i)
        else:
            last = val_arr[len(val_arr) - 1]
            if check(i, last):
                val_arr.pop()
            elif last * i > 0:
                val_arr.append(i)
            else:
                return False

    if len(val_arr) == 0:
        return True
    else:
        return False


# check is the tow values or conformed with each other
def check(a, b):
    if math.fabs(a) == math.fabs(b) and a * b < 0:
        return True
    return False


# test cases.
print(validate("([])[]({})"))
print(validate("()"))
print(validate("(})"))
