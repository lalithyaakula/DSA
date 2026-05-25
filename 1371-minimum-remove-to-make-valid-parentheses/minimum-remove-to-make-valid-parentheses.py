class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st=[]
        arr=list(s)
        for i,ch in enumerate(s):
            if ch=='(':
                st.append(i)
            elif ch==')':
                if st:
                    st.pop()
                else:
                    arr[i]=''
        while st:
            arr[st.pop()]=''
        return ''.join(arr)