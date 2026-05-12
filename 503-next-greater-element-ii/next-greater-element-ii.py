class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n
        arr=nums+nums
        st=[]
        for i in range(2*n-1,-1,-1):
            while st and st[-1]<=arr[i]:
                st.pop()
            if i<n and st:
                ans[i]=st[-1]
            st.append(arr[i])
        return ans
