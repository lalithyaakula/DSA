class Solution:
    def rotate(self, b: List[int], k: int) -> None:
        n=len(b)
        k=k%n
        temp=[0]*n
        for i in range(n):
            new_index=(i+k)%n
            temp[new_index]=b[i]
        for i in range(n):
            b[i]=temp[i]