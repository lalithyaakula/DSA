class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        ans=-1
        n=len(nums)
        if k>n:
            return ans
        l,r=max(nums),sum(nums)
        while l<=r:
            mid=(l+r)//2
            values=1
            sumi=0
            for num in nums:
                if num+sumi<=mid:
                    sumi+=num
                else:
                    values+=1
                    sumi=num
            if values<=k:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans