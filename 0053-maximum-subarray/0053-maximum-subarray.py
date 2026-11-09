class Solution(object):
    def maxSubArray(self, nums):

        largest = float('-inf')
        total = 0
        min_total = 0

        for i in range(len(nums)):
            total+=nums[i]
            largest = max(largest,total-min_total)
            min_total = min(total,min_total)
        
        return largest