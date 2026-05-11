class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix),len(matrix[0])
        l,r=0,r-1
        row=-1
        while l<=r:
            mid=(l+r)//2
            if matrix[mid][0]<=target and target<=matrix[mid][c-1]:
                row=mid
                break
            elif matrix[mid][0]>target:
                r=mid-1
            else:
                l=mid+1
        if row==-1:
            return False
        left,right=0,c-1
        while left<=right:
            mid=(left+right)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False
