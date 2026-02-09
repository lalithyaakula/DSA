class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        freq={}
        for i in nums:
            freq[i]=1+freq.get(i,0)
        for key in freq:
            if freq[key]>n//3:
                res.append(key)
        return res
