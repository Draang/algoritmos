"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copyNums=[{'index':i,'num':n} for i,n in enumerate(nums)]
        for i in range(len(copyNums)):
            for n in range(i+1,len(copyNums)):
                if copyNums[i]['num']+copyNums[n]['num']==target:
                    return [copyNums[i]['index'],copyNums[n]['index']]