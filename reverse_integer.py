class Solution:
    def reverse(self, x: int) -> int:
        
        res = str(x)
        if res[0] == '-':
            res1 = '-' + res[len(res):0:-1]
        else:
            res1 = res[::-1]

        if int(res1) >= 2 ** 31 - 1 or int(res1) <= -2 ** 31:
            return 0
        else:
            return int(res1)
