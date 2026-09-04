class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        i,j = 0,1
        for k in range(n):
            i,j=j,i+j
        return i