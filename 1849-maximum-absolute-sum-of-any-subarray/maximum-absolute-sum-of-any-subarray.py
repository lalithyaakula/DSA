class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix=0
        min_prefix=0
        max_prefix=0
        for i in range(0,len(nums)):
            prefix+=nums[i]
            min_prefix=min(min_prefix,prefix)
            max_prefix=max(max_prefix,prefix)
        return max_prefix-min_prefix


