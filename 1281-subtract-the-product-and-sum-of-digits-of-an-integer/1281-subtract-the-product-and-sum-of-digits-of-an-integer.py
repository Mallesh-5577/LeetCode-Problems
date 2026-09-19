class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = n
        product = 1
        sum = 0
        while num>0:
            digit = num%10
            product = product*digit
            sum = sum+digit
            num = num//10
        res = product-sum
        return res