from random import choices
class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        self.options = [i for i in range(len(w))]
        self.weights = []
        for weight in w:
            self.weights.append(weight/total)
        
    def pickIndex(self) -> int:
        return choices(self.options, self.weights, k=1)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
