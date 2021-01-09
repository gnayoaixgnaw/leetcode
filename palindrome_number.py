class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else: 
            c = x
            b = 0
            res = []
            while x!= 0 :
                a = x%10
                b = b*10 + a 
                x = x//10
            if c != b:
                return False
            else:
                return True
