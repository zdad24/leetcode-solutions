# Last updated: 4/30/2026, 7:59:19 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9
10        def valid(node, left, right):
11            if not node:
12                return True
13            if not (node.val < right and node.val > left):
14                return False
15            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
16
17        return valid(root, float("-inf"), float("inf"))