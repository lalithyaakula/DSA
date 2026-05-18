class Solution:
    def minLength(self, s: str) -> int:
        st=[]
        for ch in s:
            if st and ch=='B' and st[-1]=='A':
                st.pop()
            elif st and ch=='D' and st[-1]=='C':
                st.pop()
            else:
                st.append(ch)
        return len(st)

        

