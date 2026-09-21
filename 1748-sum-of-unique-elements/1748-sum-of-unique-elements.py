class Solution(object):
    def sumOfUnique(self, nums):
        dic1={}
        count=0
        for num in nums:
            if num not in dic1:
                dic1[num]=1
            else:
                dic1[num]+=1
        for num in dic1:
            if dic1[num]==1:
                count+=num
        return count