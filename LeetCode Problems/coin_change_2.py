class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        if N == 0: return int(N == amount)
        
        memo = [[0] * N for _ in range(amount + 1)]
        for i in range(N): memo[0][i] = 1
        
        for i,j in product(range(amount), range(N)):
            memo[i+1][j] = memo[i+1][j-1]
            if i+1 - coins[j] >= 0:
                memo[i+1][j] += memo[i+1-coins[j]][j]           
                    
        return memo[-1][-1]
