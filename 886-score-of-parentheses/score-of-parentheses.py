class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[0]
        for ch in s:
            if ch=="(":
                st.append(0)
            else:
                val=st.pop()
                score=max(2*val,1)
                st[-1]+=score
        return st.pop()