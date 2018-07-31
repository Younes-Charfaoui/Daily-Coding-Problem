"""This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s
and a set of all possible query strings, return all strings in the set
that have s as a prefix.

For example, given the query string de and the set of
strings [dog, deer, deal], return [deer, deal]."""


# traditional solution -_-
def auto_complete(arr, string):
    result = []
    for s in arr:
        if len(s) >= len(string):
            if string == s[:len(string)]: result.append(s)
    return result


# test
print(auto_complete(['dog', 'deer', 'deal'], 'de'))
