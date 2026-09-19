class Solution(object):
    def reverseBits(self, n):
        num = n
        add = ""
        while num>0:
            digit = num%2
            add = add + str(digit)
            num=num//2
        
        add = add + "0"*(32-len(add))
        res = int(add,2)

        return res