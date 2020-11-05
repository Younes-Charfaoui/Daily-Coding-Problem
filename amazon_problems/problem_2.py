"""This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k
distinct characters is "bcb"."""


def main(s, k):
    """
    Main function.

    Args:
        s: (int): write your description
        k: (int): write your description
    """
    start = 0
    current = ""
    max_lengths = 0
    while start < len(s):
        for i in range(start + k - 1, len(s)):
            ss = s[start:i + 1]
            counter = count_character(ss)
            if counter > k:
                break
            else:
                if len(ss) > max_lengths:
                    max_lengths = len(ss)
                    current = ss
        start += 1
    return current


def count_character(string):
    """
    Counts the number of characters in string.

    Args:
        string: (str): write your description
    """
    current = [string[0]]
    counter = 1
    for i in string:
        if i not in current:
            counter += 1
            current.append(i)
    return counter


# print(count_character("abbbcaabca"))
print(main("abbbcef", 3))
