class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m+1)]
        ans = []
        for query in queries:
            for j in range(m):
                if p[j] == query:
                    ans.append(j)
                    p = [p[j]] + p[:j] + p[j+1:]
                    break
        return ans
