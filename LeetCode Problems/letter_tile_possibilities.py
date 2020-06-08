import itertools

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = 0
        for l in range(1, len(tiles)+1): 
            combs = itertools.combinations(tiles, l)
            comb_set = set()
            for comb in combs:
                s = tuple(sorted(comb))
                if s not in comb_set:
                    comb_set.add(s)
                    perms = itertools.permutations(s)
                    perm_set = set()
                    for perm in perms:
                        if perm not in perm_set:
                            perm_set.add(perm)
                            ans += 1
        return ans
                
