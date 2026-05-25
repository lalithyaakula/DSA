class Solution:
    def smallestSubsequence(self, s: str) -> str:
        frq={}
        for i,ch in enumerate(s):
            frq[ch]=i
        st=[]
        for i,ch in enumerate(s):
            if ch in st:
                continue
            while st and st[-1]>ch and frq[st[-1]]>i:
                st.pop()
            st.append(ch)
        return ''.join(st)

        