'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''


def solution(s):
    res = 0
    for i in range(0, len(s)):
        res = res * 26 + ord(s[i]) - ord('A') + 1
    return res
