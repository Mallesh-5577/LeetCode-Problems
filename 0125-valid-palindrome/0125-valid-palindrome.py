class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=""
        for i in range(len(s)):
            if s[i].isalnum():
                s1=s1+s[i]
        s2=s1.lower()
        s3=s2[::-1]

        if s2==s3:
            return True
        else:
            return False