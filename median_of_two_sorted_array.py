class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        m = len(nums3)
        if m%2 == 0:
            return (nums3[m//2-1]+nums3[m//2])/2
        else:
            return nums3[m//2]
