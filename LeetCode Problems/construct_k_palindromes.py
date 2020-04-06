class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d = {}
        if len(s) < k:
            return False
        
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
        
        singles = 0
        
        for key in d:
            if d[key] % 2 == 1:
                singles += 1
        
        if singles > k:
            return False
        
        return True
