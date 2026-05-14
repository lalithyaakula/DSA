class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        ans=max(nums)
        hash_map={}
        for i in range(0,len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]]+=1
            else:
                hash_map[nums[i]]=1
        if hash_map[ans]!=2 :
            return False
        for i in range(1,ans):
            if i not in hash_map or hash_map[i]!=1:
                return False
        return True