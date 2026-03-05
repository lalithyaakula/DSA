class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        prefix_sum=[0]*n
        prefix_sum[0]=nums[0]
        for i in range(0,n):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        total_sum=prefix_sum[-1]
        for i in range(n):
            left_sum=prefix_sum[i-1] if i>0 else 0
            right_sum=total_sum-prefix_sum[i]
            if left_sum==right_sum:
                return i
        return -1