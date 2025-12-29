# Last updated: 12/29/2025, 3:18:51 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l = 0
4        r = len(nums)-1
5        res = 1000
6        while (l<=r):
7            mid = (r+l)//2
8            if (nums[mid] >= nums[l]):
9                res = min(res, nums[l])
10                l=mid+1
11            else:
12                res = min(res, nums[mid])
13                r=mid-1
14
15        return res