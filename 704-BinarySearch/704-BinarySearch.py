# Last updated: 12/28/2025, 2:29:12 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l = 0
4        r = len(nums) -1
5
6        while (l<=r):
7            mid = (l+r)//2
8
9            if nums[mid] == target:
10                return mid
11            elif nums[mid] > target:
12                r = mid-1
13            else:
14                l=mid+1
15
16
17        return -1