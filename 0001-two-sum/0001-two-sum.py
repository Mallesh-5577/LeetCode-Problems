class Solution(object):
    def twoSum(self, nums, target):

        dic1 = {}

        for i in range(len(nums)):
            remaining = target-nums[i]
            if remaining in dic1:
                return dic1[remaining],i
            dic1[nums[i]]=i


        