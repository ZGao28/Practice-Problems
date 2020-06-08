class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n/2 == n//2 and n > 1:
            n = n/2
        return int(n == 1)
