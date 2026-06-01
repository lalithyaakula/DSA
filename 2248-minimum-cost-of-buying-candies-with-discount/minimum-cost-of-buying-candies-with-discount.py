class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        sumi=0
        cost.sort(reverse=True)
        for i in range(len(cost)):
            if (i+1)%3!=0:
                sumi+=cost[i]
        return sumi
