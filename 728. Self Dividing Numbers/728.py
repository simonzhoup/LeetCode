'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
'''


def num(n):
    for i in str(n):
        if i == '0':
            return False
        if n % int(i) != 0:
            return False
    return True


def solution(left, right):
    return filter(num, range(left, right + 1))

# 简化


def solution_B(left, right):
    num = lambda n: all(i != '0' and n % int(i) == 0 for i in str(n))
    return filter(num, range(left, right + 1))
