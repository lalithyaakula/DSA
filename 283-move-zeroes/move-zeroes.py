class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ans=[]
        for i in range(0,len(nums)):
            if nums[i]!=0:
                ans.append(nums[i])
        zeroes=len(nums)-len(ans)
        for _ in range(zeroes):
            ans.append(0)
        for i in range(len(nums)):
            nums[i]=ans[i]
        