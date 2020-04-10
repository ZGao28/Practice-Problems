# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ranks = []
        if not root:
            return []
        def recurse(node, level):
            if level > len(ranks):
                ranks.append(node.val)
            if node.right:
                recurse(node.right, level+1)
            if node.left:
                recurse(node.left, level+1)
        recurse(root, 1)
        return ranks
