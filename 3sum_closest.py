class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dis = 999
        res = 0
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums) - 1
            while left < right :
                sums = nums[i]+nums[left] +nums[right]
                if abs(sums - target) <= dis :
                    dis = abs(sums - target)
                    res = sums
                    if (sums -target) > 0:
                        right -=1
                    elif (sums - target) <0:
                        left +=1
                    else:
                        return res
                else:
                    if (sums -target) > 0:
                        right -=1
                    elif (sums - target) <0:
                        left +=1
                    else:
                        return res
        return res
            
