class Solution(object):
    def sumBase(self, n, k):
        num = n
        add = 0
        while num>0:
            digit = num%k
            add = add + digit
            num = num//k
        return add
        