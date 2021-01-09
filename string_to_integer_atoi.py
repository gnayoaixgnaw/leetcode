class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        
        if len(s) == 0:
            return 0
        res = 0
        
        if s[0] == '-' or s[0] == '+':
            i = 2
        else :
            i = 1
        
        while i <= len(s):
            try:
                res = int(s[:i])
                i+=1
            except:
                break
        if res < -2147483648:
            return -2147483648
        if res > 2147483647:
            return 2147483647
        
        return res
