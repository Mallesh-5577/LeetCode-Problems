class Solution(object):
    def findMissingElements(self, nums):
        n = sorted(nums)
        first = n[0]
        last = n[-1]

        missing = []

        for i in range(first,last+1):
            if i not in n:
                missing.append(i)
        return missing
