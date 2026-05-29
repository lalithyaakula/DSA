class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=[]
        for n in nums:
            total=0
            for ch in str(n):
                total+=int(ch)
            ans.append(total)
        return min(ans)
        


