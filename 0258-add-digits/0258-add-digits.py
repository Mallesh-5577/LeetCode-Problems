class Solution(object):
    def addDigits(self, num):
        n = num
        while n>=10:
            add = 0
            while n>0:
                digit = n%10
                add = add + digit
                n = n//10
            n = add
        return n 
        