class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}

        for word in strs:

            sorted_word = "".join(sorted(word))

            if sorted_word not in group:
                group[sorted_word] = []
                
            group[sorted_word].append(word)
        
        return group.values()