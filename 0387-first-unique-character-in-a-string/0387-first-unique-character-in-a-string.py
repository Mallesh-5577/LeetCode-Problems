class Solution(object):
    def firstUniqChar(self, s):

        dic1={}

        for char in s:
            if char not in dic1:
                dic1[char]=1
            else:
                dic1[char]+=1
        
        for i in range(len(s)):
            if dic1[s[i]]==1:
                return i
        return -1