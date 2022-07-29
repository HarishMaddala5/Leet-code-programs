class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c=0
        l=[]
        for i in nums:
            c+=i
            l.append(c)
        return l