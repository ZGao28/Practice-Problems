from sortedcontainers import SortedSet
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.memo = [{} for _ in range(len(arr))]
        self.arr = arr
        return self.recurse(SortedSet(), 0)
        
    def recurse(self, seen, i):
        if i == len(self.arr):
            return len(seen)
        if seen and tuple(seen) in self.memo[i]:
            return self.memo[i][tuple(seen)]
        paths = [len(seen)]
        for j in range(i, len(self.arr)):
            unique = True
            new_seen = seen.copy()
            for char in self.arr[j]:
                if char in new_seen:
                    unique = False
                    break
                new_seen.add(char)
            if unique:
                paths.append(self.recurse(new_seen, j+1))
        ans = max(paths)
        self.memo[i][tuple(seen)] = ans
        return ans
