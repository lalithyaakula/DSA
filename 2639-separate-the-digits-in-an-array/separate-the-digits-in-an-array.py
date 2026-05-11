class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums:
            temp=[]
            while num>0:
                digit=num%10
                temp.append(digit)
                num=num//10
            for i in range(len(temp)-1,-1,-1):
                ans.append(temp[i])
        return ans