class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi=0
        l,zero_ct=0,0
        for r in range(0,len(nums)):
            if nums[r]==0:
                zero_ct+=1
            while zero_ct>k:
                if nums[l]==0:
                    zero_ct-=1
                l+=1
            maxi=max(maxi,r-l+1)
        return maxi