class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        avg=window_sum/k
        max_avg=avg
        for i in range(len(nums)-k):
            window_sum=window_sum-nums[i]+nums[i+k]
            avg=window_sum/k
            max_avg=max(max_avg,avg)
        return max_avg
