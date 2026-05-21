class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        set1=set()
        for i in range(len(arr1)):
            num=str(arr1[i])
            for j in range(1,len(num)+1):
                prefix=num[:j]
                set1.add(prefix)
        ans=0
        for number in arr2:
            number=str(number)
            for i in range(len(number),0,-1):
                prefix2=number[:i]
                if prefix2 in set1:
                    ans=max(ans,len(prefix2))
                    break
        return ans


        