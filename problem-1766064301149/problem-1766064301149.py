# Last updated: 12/18/2025, 8:25:01 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        ans = []
4        nums.sort()
5        
6        for i, a in enumerate(nums):
7            if i > 0 and a == nums[i-1]:
8                continue
9            l = i+1
10            r = len(nums)-1
11            while (l < r):
12                threeSum = a + nums[l] + nums[r]
13                if (threeSum == 0):
14                    ans.append([a, nums[l], nums[r]])
15                    l +=1
16                    while nums[l] == nums[l-1] and l < r:
17                        l+=1
18                elif (threeSum > 0):
19                    r-=1
20                else:
21                    l+=1
22        return ans