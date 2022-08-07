class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s+=str(i)
        d=int(s)
        l=list(map(int,list(str(d+1))))
        return l