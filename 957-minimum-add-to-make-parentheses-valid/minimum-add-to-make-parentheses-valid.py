class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        for ch in s:
            if ch =="(":
                st.append(ch)
            else:
                if st and st[-1]=="(":
                    st.pop()
                else:
                    st.append(ch)
        return len(st)