class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = {}
        result = False

        for i in range(len(nums)):
            if nums[i] in hash_map:
                last_index = hash_map[nums[i]]
                if i - last_index <= k:
                    result = True
                    break
            hash_map[nums[i]] = i

        return result