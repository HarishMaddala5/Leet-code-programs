class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n1=nums[0]*nums[1]
        n2=nums[(len(nums)-1)]*nums[(len(nums)-2)]
        return n2-n1