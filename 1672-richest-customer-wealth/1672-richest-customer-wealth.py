class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        c=0
        l=[]
        for i in accounts:
            for j in i:
                c+=j
            l.append(c)
            c=0
        l.sort()
        return l[len(l)-1]