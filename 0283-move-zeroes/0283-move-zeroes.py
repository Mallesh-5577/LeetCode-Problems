class Solution(object):
    def moveZeroes(self, nums):
        mov = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[mov],nums[i]=nums[i],nums[mov]
                        
                mov+=1
        return nums
        
