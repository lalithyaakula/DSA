class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        for w in s.split():
            res.append(w[::-1])
        return " ".join(res)
        
       