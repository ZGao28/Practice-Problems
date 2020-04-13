class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ans += self.distance(nums[i], nums[j])
        return ans
    
    def distance(self, n1, n2):
        if n1 == n2:
            return 0
        
        l = int(math.floor(math.log(max(n1, n2), 2))) + 1
        n1_bits = [0 for _ in range(l)]
        n2_bits = [0 for _ in range(l)]
        
        while n1 > 0:
            log = int(math.floor(math.log(n1, 2)))
            n1_bits[log] = 1
            n1 -= 2**log
        
        while n2 > 0:
            log = int(math.floor(math.log(n2, 2)))
            n2_bits[log] = 1
            n2 -= 2**log
            
        count = 0
        for i in range(l):
            if n1_bits[i] != n2_bits[i]:
                count += 1
        return count
