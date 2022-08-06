class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=list(s.split())
        n=l[len(l)-1]
        return len(n)