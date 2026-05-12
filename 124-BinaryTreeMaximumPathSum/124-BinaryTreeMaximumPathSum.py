# Last updated: 5/11/2026, 8:04:01 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        res = [root.val]
10
11        def dfs(root):
12            if not root:
13                return 0
14            leftMax = dfs(root.left)
15            rightMax = dfs(root.right)
16            leftMax = max(0, leftMax)
17            rightMax = max(0, rightMax)
18
19            res[0] = max(res[0], root.val + leftMax + rightMax) #calculate bend
20            return root.val + max(leftMax, rightMax) #pick best leg, left or right
21        
22        dfs(root)
23        return res[0]