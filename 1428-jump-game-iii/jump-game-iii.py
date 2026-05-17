from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        q=deque([start])
        visited=set([start])
        while q:
            i=q.popleft()
            if arr[i]==0:
                return True
            left=i-arr[i]
            right=i+arr[i]
            if left>=0 and left not in visited:
                visited.add(left)
                q.append(left)
            if right<n and right not in visited:
                visited.add(right)
                q.append(right)
        return False
        