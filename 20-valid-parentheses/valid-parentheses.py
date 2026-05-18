class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch in"{[(":
                st.append(ch)
            elif ch==')'or ch=='}' or ch==']':
                if not st:
                    return False
                elif ch==')' and st.pop()!='(':
                    return False
                elif ch=='}' and st.pop()!='{':
                    return False
                elif ch==']' and st.pop()!='[':
                    return False
            else:
                return False
        return not st