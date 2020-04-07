class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1, n+1):
            s = str(i)
            su = 0
            for c in s:
                su += int(c)
            if su not in d:
                d[su] = 0
            d[su] += 1
        ans, m = 0, 0
        for k in d:
            if d[k] == m:
                ans += 1
            if d[k] > m:
                ans = 1
                m = d[k]
        return ans
