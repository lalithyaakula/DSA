class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st=[]
        for i,ch in enumerate(s):
            if ch in st:
                continue 
            while st and st[-1]>ch and st[-1] in s[i+1:]:
                st.pop()
            st.append(ch)
        return ''.join(st)