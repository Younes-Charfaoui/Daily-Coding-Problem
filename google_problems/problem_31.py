"""This problem was asked by Google.
Given a string of parentheses, write a function to compute the minimum number of parentheses to be 
removed to make the string valid (i.e. each open parenthesis is eventually closed).
For example, given the string "()())()", you should return 1. 
Given the string ")(", you should return 2, since we must remove all of them."""

string = "()())()"
string = ")("
string = ")()"
string = "()()"
string = "()(())()"

status = False
result = 0

for i in string:
    if i == "(" and not status:
        status= True
        result += 1
    elif i == "(" and status:
        result += 1
    elif i==")" and status:
        status = False
        result -= 1
    elif i == ")" and not status:
        result += 1
    
print(abs(result))
        