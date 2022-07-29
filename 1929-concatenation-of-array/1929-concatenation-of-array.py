class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            l.append(i)
        for j in nums:
            l.append(j)
        return l