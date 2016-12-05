# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    """Return (i, j) such that text[i:j] is the longest palindrome in text."""
    # Your code here
    oddLetters = [(i,j) for (i,j) in enumerate(text.lower()) if i % 2 == 1 and j==j]
    for prospect in oddLetters:
        if check_palindrome(text[i:j]):
            return (i, j)
    # get the string
    #
    # how to check if palindrome,
    # join the string
    # reversed the string, and join
    # if these two var is same, then true

    'something rac e car going'

    """
    the palindrome should be odd num of string
    create the enumerate of odd index str
    if the odd indices str is same,
    retreive the str from text
    check if it is palindrome
    sort max of that indices, by using abs(i-j)

    """

# def check_oddletters(text):
#     oddLetters = [(i,j) for (i,j) in enumerate(text) if i % 2 == 1 and j==j]
#     for prospect in oddLetters:
#         if check_palindrome(text[i:j]):
#             return (i, j)

def check_palindrome(str):
    strings = str.split('').join().tolowercaes()
    reversedstr = reversed(strings)
    if strings == reversedstr:
        return True



def test():
    L = longest_subpalindrome_slice
    assert L('something rac e car going') == (8, 21)
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


print test()