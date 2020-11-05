"""TThis problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: 
"A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. 
For example, given 1, return "A". Given 27, return "AA"."""

def spreadsheet(number):
    """
    Returns a number.

    Args:
        number: (int): write your description
    """
    return number//26 + 1

spreadsheet(27)	