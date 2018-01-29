'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''


def solution(num):
    def xx(n):
        return sum([int(i) for i in list(str(n))])
    while num > 9:
        num = xx(num)
    return num


def solution2(num):
    if num == 0:
        return 0
    else:
        return (num - 1) % 9 + 1
