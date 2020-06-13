class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        nums.sort()
        memo = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(memo[i]) < len(memo[j]) + 1:
                    memo[i] = memo[j] + [nums[i]]
        return max(memo, key=len)
        
