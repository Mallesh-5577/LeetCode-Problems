class Solution(object):
    def checkPerfectNumber(self, num):
        n=num
        res = []
        for i in range(1,int(sqrt(n))+1):
            if num%i==0:
                res.append(i)
                if num//i != i:
                    res.append(num//i)
        res.sort()

        add = 0
        for j in range(len(res)-1):
            add = add+res[j]
        if num==add:
            return True
        else:
            return False


        