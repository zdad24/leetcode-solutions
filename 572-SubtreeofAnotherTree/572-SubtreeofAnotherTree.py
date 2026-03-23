# Last updated: 3/23/2026, 5:22:45 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9        if not subRoot:
10            return True
11        if not root:
12            return False
13        if self.isSameTree(root, subRoot):
14            return True
15        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
16
17    def isSameTree(self, t, s):
18        if not t and not s:
19            return True
20        if t and s and t.val == s.val:
21            return self.isSameTree(t.left, s.left) and self.isSameTree(t.right, s.right)
22        return False