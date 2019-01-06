"""This problem was asked by Facebook.

Given a start word, an end word, and a dictionary of valid words, 
find the shortest transformation sequence from start to end such that only one letter 
is changed at each step of the sequence, and each transformed word exists in the dictionary. 
If there is no possible transformation, return null. 
Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, 
return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, 
return null as there is no possible transformation from dog to cat.
"""