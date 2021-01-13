class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            left = i+1
            right = len(nums)-1
            
            while left < right :
                sums = nums[i]+nums[left] +nums[right]
                if sums == 0:
                    temp = [nums[i],nums[left],nums[right]]
                    
                    if temp not in res:
                        res.append(temp)
                    left +=1
                    right -=1
                elif sums <0:
                    left +=1
                else:
                    right -=1
        return res
