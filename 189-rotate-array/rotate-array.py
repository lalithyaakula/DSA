class Solution:
    def rotate(self, b: List[int], k: int) -> None:
        n=len(b)
        k%=n
        def reverse(l,r):
            while l<r:
                b[l],b[r]=b[r],b[l]
                l+=1
                r-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        