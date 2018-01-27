'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.



Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''


def solution(words):
    top = 'qwertyuiopQWERTYUIOP'
    conter = 'asdfghjklASDFGHJKL'
    botten = 'zxcvbnmZXCVBNM'
    a = []
    for word in words:
        for k in [top, conter, botten]:
            if all([w in k for w in word]):
                a.append(word)
    return a
