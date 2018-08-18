"""This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single
count and character. For example, the string "AAAABBBCCDAA" would be
encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits
and consists solely of alphabetic characters.
You can assume the string to be decoded is valid """


def main(string):
    if len(string) == 0:
        return ""
    else:
        current = string[0]
        counter = 0
        output = ""
        for i in string:
            if current == i:
                counter += 1
            else:
                output += str(counter) + current
                counter = 1
                current = i
        output += str(counter) + current
        return output
print(main("AAAABBBCCDAA"))