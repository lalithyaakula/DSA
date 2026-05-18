class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        mp = defaultdict(list)
        for i, num in enumerate(arr):
            mp[num].append(i)
        q = deque([0])
        visited = set([0])
        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                i = q.popleft()
                if i == n - 1:
                    return steps
                neighbors = []
                neighbors.extend(mp[arr[i]])
                if i + 1 < n:
                    neighbors.append(i + 1)
                if i - 1 >= 0:
                    neighbors.append(i - 1)
                for nei in neighbors:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
                mp[arr[i]].clear()
            steps += 1