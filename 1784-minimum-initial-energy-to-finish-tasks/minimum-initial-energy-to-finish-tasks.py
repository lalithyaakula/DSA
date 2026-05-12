class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)
        l = 1
        r = sum(task[1] for task in tasks)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            energy = mid
            possible = True
            for actual, minimum in tasks:
                if energy < minimum:
                    possible = False
                    break
                energy -= actual
            if possible:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans