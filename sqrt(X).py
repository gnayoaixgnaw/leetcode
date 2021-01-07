class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x//2+1

        while left < right:
            mid = (left + right)//2+1
            squ = mid*mid
            if squ > x:
                right = mid-1
            else:
                left = mid
        return left
