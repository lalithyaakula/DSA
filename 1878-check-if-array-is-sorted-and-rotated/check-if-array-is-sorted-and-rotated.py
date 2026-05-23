class Solution:
    def check(self, nums: List[int]) -> bool:
        a=len(nums)
        count=0
        for i in range(0,a):
            if nums[i]>nums[(i+1)%a]:
                count+=1
                if count>1:
                    return False
        return True