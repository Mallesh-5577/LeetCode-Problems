class Solution(object):
    def groupAnagrams(self, strs):
        dic1 = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in dic1:
                dic1[key] = []
            dic1[key].append(word)
        final_strs = list(dic1.values())

        return final_strs