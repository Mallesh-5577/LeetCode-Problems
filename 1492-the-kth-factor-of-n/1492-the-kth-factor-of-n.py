class Solution(object):
    def kthFactor(self, n, k):
        num = n
        add = []
        for i in range(1,int(sqrt(n))+1):
            if num%i==0:
                add.append(i)
                if num//i != i:
                    add.append(num//i)
        add.sort()
 
        if k > len(add):
            return -1
        res = 0
        for j in range(k):
            res = add[j]
        return res
                
        