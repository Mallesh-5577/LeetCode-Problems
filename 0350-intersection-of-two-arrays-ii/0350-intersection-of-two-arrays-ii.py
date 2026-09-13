class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count={}
        result=[]
        for i in nums2:
            if i in count:
                count[i]=count[i]+1
            else:
                count[i]=1
        
        for i in nums1:
            if i in count and count[i]>0:
                result.append(i)
                count[i]=count[i]-1
        return result