class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        count = 0
        max_count = 0
        last_num = float("-inf")

        for i in range(len(nums)):
            num = nums[i]
            if num-1 == last_num:
                count+=1
                last_num = num
            elif num!=last_num:
                count=1
                last_num = num
            max_count = max(max_count,count)
        return max_count