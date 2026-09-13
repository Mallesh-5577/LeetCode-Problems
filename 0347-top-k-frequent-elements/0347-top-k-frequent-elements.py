class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = {}
        for i in range(len(nums)):
            keys = nums[i]
            if keys not in ans:
                ans[keys] = 1
            else:
                ans[keys] +=1

        sorted_res = sorted(ans, key=ans.get, reverse=True)

        res = sorted_res[:k]
        
        return res