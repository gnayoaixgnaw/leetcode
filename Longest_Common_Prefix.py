class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        else:
            res = strs[0]
            for s in strs[1:]:
                temp = ''
                for i,j in zip(res,s):
                    if i == j:
                        temp +=i
                    else:
                        break
                if temp:
                    res = temp
                else:
                    return ''
            return res
