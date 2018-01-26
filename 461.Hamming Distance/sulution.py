'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

from collections import Counter


def solution(x, y):
    '''先使用位运算符 ^：当两对应的二进位相异时，结果为1，然后用Counter 方法计算1的次数'''
    return Counter(bin(x ^ y))['1']
