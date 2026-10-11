class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        posIndex=0
        negIndex = 1

        for i in range(len(nums)):
            if nums[i]>=0:
                res[posIndex]=nums[i]
                posIndex+=2
            else:
                res[negIndex]=nums[i]
                negIndex+=2
        return res