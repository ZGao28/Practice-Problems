class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        for cost in costs:
            diffs.append((abs(cost[1]-cost[0]), cost))
        diffs.sort(reverse = True)
        
        a = b = len(costs)//2
        ans = 0
        for elem in diffs:
            if (b == 0 or elem[1][0] < elem[1][1]) and a > 0:
                a -= 1
                ans += elem[1][0]
            else:
                b -= 1
                ans += elem[1][1]
        return ans
