class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people, ans = sorted(people, key=lambda x:(-1*x[0],x[1])), []
        for p in people:
            ans.insert(p[1],p)
        return ans
