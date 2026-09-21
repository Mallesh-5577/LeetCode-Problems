class Solution(object):
    def intersection(self, nums1, nums2):
        dic1={}
        res=[]
        for num in nums1:
            dic1[num]=1
        for num in nums2:
            if num in dic1 and dic1[num]==1:
                res.append(num)
                dic1[num]=0
        return res