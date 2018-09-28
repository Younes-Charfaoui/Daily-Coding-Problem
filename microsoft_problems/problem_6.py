"""This problem was asked by Microsoft.
Given a 2D matrix of characters and a target word, write a function that returns
whether the word can be found in the matrix by going left-to-right, or up-to-down.
For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. 
Similarly, given the target word 'MASS', 
you should return true, since it's the last row.
"""

matrix = [['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']]

requested_word = "IPBS"


def get_all_words():
    result = []
    current = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            current += matrix[i][j]
        result.append(current)
        current = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            current += matrix[j][i]
        result.append(current)
        current = ""
    return result


words = get_all_words()


if requested_word in words:
    print(True)
else:
    print(False)
