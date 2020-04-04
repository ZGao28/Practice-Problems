class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        dp, sum = [0], 0
        for num in satisfaction:
            dp.append(num+dp[-1]+sum)
            sum += num
        return max(dp)
