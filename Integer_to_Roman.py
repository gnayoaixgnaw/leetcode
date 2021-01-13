class Solution:
    def intToRoman(self, num: int) -> str:
        
        d = {1:"I", 4: "IV", 5:"V", 9:"IX", 10:"X", 40: "XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900: "CM", 1000: "M"}
    
        if num in d.keys():
            return d[num]
    
        res = ""
    
        for k in list(d.keys())[::-1]:
            if num < k:
                pass
            else:
                while num >= k:
                    num = num - k
                    res += d[k]
            
        return res
