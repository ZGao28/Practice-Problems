class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans, diff, d = 0, 0, {0: -1}
        for i, num in enumerate(nums):
            diff += 2*num - 1
            if diff not in d:
                d[diff] = i
            ans = max(ans, i-d[diff])
        return ans
