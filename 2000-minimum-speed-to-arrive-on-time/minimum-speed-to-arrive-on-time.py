class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l,r=1,10**7
        ans=-1
        while l<=r:
            mid=(l+r)//2
            total=0
            for i in range(0,len(dist)-1):
                total+=(dist[i]+mid-1)//mid
            total+=dist[-1]/mid
            if total<=hour:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans

