class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            temp = list(range(n))
            temp[0] = 1
            temp[1] = 2
            for i in range(2,n):
                temp[i]=temp[i-1]+temp[i-2]
            return temp[n-1]
