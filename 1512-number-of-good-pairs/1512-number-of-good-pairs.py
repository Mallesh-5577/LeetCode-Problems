class Solution(object):
    def numIdenticalPairs(self, nums):

        dic1={}
        count=0

        for num in nums:
            if num not in dic1:
                dic1[num] = 1
            else:
                count+=dic1[num]
                dic1[num]+=1
        return count