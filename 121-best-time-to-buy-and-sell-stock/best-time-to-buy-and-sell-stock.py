class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       pro=0
       l,r=0,1
       while r<len(prices):
        if prices[l]<prices[r]:
            ans=prices[r]-prices[l]
            pro=max(ans,pro)
        else:
            l=r
        r+=1
       return pro