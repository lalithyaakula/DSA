class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,sumo=0,0
        mini=float('inf')
        for r in range(0,len(nums)):
            sumo+=nums[r]
            while sumo>=target:
                mini=min(mini,r-l+1)
                sumo-=nums[l]
                l+=1
        return 0 if mini==float('inf') else mini