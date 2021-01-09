class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        else:
            step = 1
            cursor = 0
            res = ['']*numRows
            
            for i in s:
                res[cursor]+=i
                cursor+=step
                if cursor == 0 or cursor == numRows-1:
                    step = -step
            return ''.join(res)
