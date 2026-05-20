class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA=set()
        setB=set()
        common=0
        ans=[]
        for i in range(len(A)):
            if A[i]==B[i]:
                common+=1
            else:
                if A[i] in setB:
                    common+=1
                if B[i] in setA:
                    common+=1
            setA.add(A[i])
            setB.add(B[i])
            ans.append(common)
        return ans
