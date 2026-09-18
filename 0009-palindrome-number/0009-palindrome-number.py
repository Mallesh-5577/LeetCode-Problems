class Solution(object):
    def isPalindrome(self, x):
        num = x
        rev = 0
        while num>0:
            digit = num%10
            rev = rev*10 + digit
            num = num//10
        if rev==x:
            return True
        else:
            return False
        