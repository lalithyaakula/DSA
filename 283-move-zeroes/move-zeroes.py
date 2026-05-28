class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
         l,r=0,1
         while r<len(nums):
            if nums[l]==0 and nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
            elif nums[l]==0 and nums[r]==0:
                r+=1
            else:
                l+=1
                r+=1
