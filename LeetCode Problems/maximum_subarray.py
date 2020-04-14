class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = 0
        count_at_iterator = 0
        for i in range(len(nums)):
            count_at_iterator += nums[i]
            if count_at_iterator < 0:
                count_at_iterator = 0
            elif count_at_iterator > current_max:
                current_max = count_at_iterator
        if current_max == 0 and len(nums) > 0:
            current_max = max(nums)
        return current_max
