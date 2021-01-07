class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = '0'*(len(a)- len(b)) + b
        else:
            a = '0'*(len(b)- len(a)) + a
            
        status = 0
        res = ''
        for i in range(len(a)-1, -1, -1):
            if (int(a[i]) + int(b[i]) + status ) >=2:
                res = str(int(a[i]) + int(b[i]) + status -2)+res
                status = 1
            else:
                res = str(int(a[i]) + int(b[i])+ status)+res
                status = 0
        if status ==1:
            res = '1' + res
        
        return res
