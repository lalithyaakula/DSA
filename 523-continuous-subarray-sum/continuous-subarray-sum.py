class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        pre_sum=0
        hash_map={0:-1}
        for i in range(0,n):
            pre_sum+=nums[i]
            rem=pre_sum%k
            if rem in hash_map:
                if i-hash_map[rem]>=2:
                    return True
            else:
                hash_map[rem]=i
        return False

        