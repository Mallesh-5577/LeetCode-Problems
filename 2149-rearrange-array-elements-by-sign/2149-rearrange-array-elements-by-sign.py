class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        
        for j in range(len(pos)):
            nums[j*2] = pos[j]
            nums[(j*2)+1] = neg[j]
        
        return nums