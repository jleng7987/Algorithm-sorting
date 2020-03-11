# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            a = self.maxDepth(root.left)
            b = self.maxDepth(root.right)
            return  max(a,b)+1

# 思路，就是递归，找每一层的数量，
# 左边的树和右边的树的叶子那个深要哪哥，递归还要多练习，总糊涂