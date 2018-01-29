'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''


def solution(nums):
    for n in nums:
        if nums.count(n) == 1:
            return n


def solution2(nums):
    res = 0
    for n in nums:
        res ^= n
    return res
