'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
'''


def solution(num):
    n = '0b'
    for i in bin(num)[2:]:
        n += '0' if i == '1' else '1'
    return eval(n)


def solution_B(num):
    i = 1
    while i <= num:
        i = i << 1
    return (i - 1) ^ num
