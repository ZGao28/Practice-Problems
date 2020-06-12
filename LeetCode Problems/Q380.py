import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict:
            return False
        ind = self.dict[val]
        self.dict[self.arr[-1]] = ind
        self.arr[ind], self.arr[-1] = self.arr[-1], self.arr[ind]
        del self.dict[val]
        del self.arr[-1]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
