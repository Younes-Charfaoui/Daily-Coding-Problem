"""This problem was asked by Google.
The edit distance between two strings refers to the minimum 
number of character insertions, deletions, and substitutions 
required to change one string to the other. For example, 
the edit distance between “kitten” and “sitting” is three: 
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
Given two strings, compute the edit distance between them."""


def compare(first,second):
    if len(first) > len(second):
        return first
    return second

def compute_edit_distance(first,second):
    substitute = 0
    bigger = compare(first, second)
    for i in range(len(bigger)):
        try:
            if first[i] != second[i]:
                substitute += 1
        except :
            substitute += 1
    return substitute

substitute = compute_edit_distance("kitten","sitting")
print("sub =",substitute)