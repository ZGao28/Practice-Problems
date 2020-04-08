class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 0
            d[num] += 1
        ans = 0
        for key in d:
            if d[key] == key:
                ans = max(ans, key)
        if ans == 0:
            return -1
        return ans
                
