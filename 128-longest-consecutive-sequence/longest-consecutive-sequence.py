class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer=set(nums)
        longest=0
        for num in answer:
            if num-1 not in answer:
                length=1
                while num+length in answer:
                    length+=1
                longest=max(longest,length)
        return longest
