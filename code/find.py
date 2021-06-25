# Creates a list containing indices of a specified character in a string

def findExpression(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]