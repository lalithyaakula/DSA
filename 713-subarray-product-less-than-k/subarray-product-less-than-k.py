class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        prod=1
        left,count=0,0
        for r in range(0,len(nums)):
            prod*=nums[r]
            while prod>=k:
                prod//=nums[left]
                left+=1
            count+=r-left+1
        return count