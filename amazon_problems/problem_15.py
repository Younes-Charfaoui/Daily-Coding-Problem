"""This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, 
since it can be rearranged to form racecar, which is a palindrome. 
daily should return false, since there's no rearrangement that can form a palindrome.
"""
#idea : we can't have more than one letter that has an odd frequency
def solve(s):
    freq = [0] * 256
    for c in s:
        freq[ord(c)] += 1

    cp = 0
    for f in freq:
        cp += f & 1
        
    return cp <= 1


print(solve('daily')) # returns False
print(solve('carrace')) #returns True
