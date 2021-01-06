class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(len(nums)):
            temp = target - nums[i]
            
            if temp in dic.keys():
                return [dic[temp],i]
            else:
                dic[nums[i]] = i
        
