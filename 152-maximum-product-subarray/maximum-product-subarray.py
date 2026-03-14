class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        prefix_product=1
        suffix_product=1
        ans=float('-inf')
        for i in range(0,n):
            prefix_product*=nums[i]
            suffix_product*=nums[n-i-1]
            ans=max(ans,prefix_product,suffix_product)
            if prefix_product==0:
                prefix_product=1
            if suffix_product==0:
                suffix_product=1
           
        return ans
