class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        max_area=0
        st=[]
        for i in range(n+1):
            if i==n:
                h=0
            else:
                h=heights[i]
            while st and h<heights[st[-1]]:
                height=heights[st.pop()]
                width=i if not st else i-st[-1]-1
                max_area=max(max_area,height*width)
            st.append(i)
        return max_area
        