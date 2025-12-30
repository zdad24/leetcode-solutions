# Last updated: 12/30/2025, 4:31:31 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l = 0
4        r = len(nums)-1
5
6        while(l<=r):
7            mid = (l+r)//2
8            if nums[mid] == target:
9                return mid
10            
11            #left sorted portion
12            if nums[mid] >= nums[l]:
13                if target >= nums[l] and target < nums[mid]:
14                    r = mid - 1  # target is in left sorted portion
15                else:
16                    l = mid + 1  # target is in right portion
17                    
18            #right sorted portion
19            else:
20                if target > nums[mid] and target <= nums[r]:
21                    l = mid + 1  # target is in right sorted portion
22                else:
23                    r = mid - 1  # target is in left portion
24                    
25        return -1