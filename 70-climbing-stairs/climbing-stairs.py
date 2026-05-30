class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[-1]*(n+1)
        return self.helper(n,arr)

    def helper(self,n,arr):
        if n<=3:
            return n
        if arr[n]!=-1:
            return arr[n]
        arr[n]=self.helper(n-1,arr)+self.helper(n-2,arr)
        return arr[n]