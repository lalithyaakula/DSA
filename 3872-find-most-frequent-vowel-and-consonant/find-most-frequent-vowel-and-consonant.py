class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow='aeiou'
        v=[]
        c=[]
        for i in s:
            if i in vow:
                v.append(i)
            else:
                c.append(i)
        x=v.count(mode(v)) if v else 0
        y=c.count(mode(c)) if c else 0
        return x+y