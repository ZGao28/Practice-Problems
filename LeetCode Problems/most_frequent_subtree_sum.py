# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        d = {}
        if not root:
            return []
        def recurse(root):
            s = root.val
            if root.left:
                s += recurse(root.left)
            if root.right:
                s += recurse(root.right)
            if s not in d:
                d[s] = 0
            d[s] += 1
            return s
        recurse(root)
        curr = 0
        ans = []
        for key in d:
            if d[key] == curr:
                ans.append(key)
            if d[key] > curr:
                ans = [key]
                curr = d[key]
        return ans
            
