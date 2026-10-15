'''
Traditional Brute Force approach.
There are two lists. If I start with the first element and check its sum with every other element
So in loop 1 of the inner loop, value 1 is checked with all other elements
In loop 2 of inner loop, value 2 is checked with all other elements.
If the index is same then discard since that is the condition. 
Also since every input is supposed to have a solution there is no fallback condition in case
Loop in loop so pretty heavy - O(n^2)
'''

# 3512 ms | 19.7 MB

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if index1 == index2:
                    continue
                if num1+num2 == target:
                    return [index1, index2]

'''
Hash Map solution maybe ?
'''