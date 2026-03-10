class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hash_map={0:1}
        count=0
        ans=0
        for i in range(0,len(nums)):
            ans+=nums[i]
            mod=ans%k
            if mod in hash_map:
                count+=hash_map[mod]
                hash_map[mod]+=1
            else:
                hash_map[mod]=1
        return count



        