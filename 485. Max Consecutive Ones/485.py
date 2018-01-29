'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''


def solution(nums):
    res = []
    x = 0
    for n in nums:
        if n != 0:
            x += 1
        elif n == 0:
            res.append(x)
            x = 0
    res.append(x)
    return max(res)


print solution([1])
