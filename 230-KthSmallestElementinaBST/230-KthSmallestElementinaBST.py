# Last updated: 5/9/2026, 3:25:09 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        n = 0
10        curr = root
11        stack = []
12
13        while curr or stack:
14            while curr:
15                stack.append(curr)
16                curr = curr.left
17            curr = stack.pop()
18            n += 1
19            if n == k:
20                return curr.val
21            curr = curr.right