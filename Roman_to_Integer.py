class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i=0
        res=0
        
        while i <= len(s)-1:
            if(s[i] != 'I' and s[i] != 'X' and s[i] != 'C'):
                res+=dic[s[i]]
            else:
                if(i+1 <= len(s)-1):
                    if(s[i]+s[i+1] in dic):
                        res+=dic[s[i]+s[i+1]]
                        i+=1
                    else:
                        res+=dic[s[i]]  
                else:
                    res+=dic[s[i]]
            
            i+=1
        
        return res
