class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        sub = ""
        sub2 = ''
        for i in range(n):
            
			#pick each element as the potential "center" of a palindrome
            left = i
            right = i + 1
            while left >= 0 and right <= n and s[left:right] == s[left:right][::-1]:
				
				#continue radiating outwards until you've found
				#the largest palindrome at that center
				
                sub = s[left:right] if right - left > len(sub) else sub
                left -= 1
                right += 1
                
        for i in range(n - 1):
            if s[i] == s[i+1]:
                left = i
                
                #repeat the same process, but for
                #even-numbered palindromes
                
                right = i + 2
                while left >= 0 and right <= n and s[left:right] == s[left:right][::-1]:
                    sub2 = s[left:right] if right - left > len(sub2) else sub2
                    left -= 1
                    right += 1
        
        if len(sub) >= len(sub2):
            return sub
        else:
            return sub2
