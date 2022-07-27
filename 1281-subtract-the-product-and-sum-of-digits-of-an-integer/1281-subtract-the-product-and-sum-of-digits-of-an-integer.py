class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=list(map(int,list(str(n))))
        c1=1
        c2=0
        for i in temp:
            c1*=i
            c2+=i
        return (c1-c2)
            