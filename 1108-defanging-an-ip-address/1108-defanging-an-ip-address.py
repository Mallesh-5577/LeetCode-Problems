class Solution(object):
    def defangIPaddr(self, address):
        
        ans = address.replace('.','[.]')
        return ans