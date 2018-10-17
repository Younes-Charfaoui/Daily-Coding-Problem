"""This question was asked by ContextLogic.

Implement division of two positive integers without using the division, 
multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder."""

# main method for making division, quiet easy: just subtract second nomber for the first until 0. and count.
def division(a,b):
    i=0
    while a >= b:
        i += 1
        a = a-b
    return i

print(division(6,2))
print(division(10,5))
print(division(20,5))
print(division(120,20))
        