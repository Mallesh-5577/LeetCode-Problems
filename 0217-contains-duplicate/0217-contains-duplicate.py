class Solution(object):
    def containsDuplicate(self, nums):

        dic1 = {}
        for i in range(len(nums)):
            if nums[i] in dic1:
                return True
                break
            else:
                dic1[nums[i]]=i
        return False
