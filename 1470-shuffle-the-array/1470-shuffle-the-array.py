class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1=[]
        l2=[]
        l=[]
        for i in range(n):
            l1.append(nums[i])
        for j in range(n,(len(nums))):
            l2.append(nums[j])
        for k in range(n):
            l.append(l1[k])
            l.append(l2[k])
        return l
            