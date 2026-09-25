class Solution(object):
    def thirdMax(self, nums):
        res = sorted(set(nums), reverse=True)
        if len(res)>=3:
            return res[2]
        return res[0]
        