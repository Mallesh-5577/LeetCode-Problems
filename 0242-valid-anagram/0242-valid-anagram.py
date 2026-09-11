class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}

        for i in range(len(s)):
            key1 = s[i]
            if key1 not in dic1:
                dic1[key1] = 1
            else:
                dic1[key1] += 1
        for j in range(len(t)):
            key2  = t[j]
            if key2 not in dic2:
                dic2[key2] = 1
            else:
                dic2[key2]+=1
        if dic1==dic2:
            return True
        else:
            return False