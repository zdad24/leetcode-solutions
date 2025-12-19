# Last updated: 12/19/2025, 8:02:20 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        l = 0
4        r = len(height)-1
5        maxarea = 0
6        while (l < r):
7            tall = min(height[l], height[r])
8            width = r - l
9            area = tall*width
10            maxarea = max(maxarea, area)
11            if (height[l] > height[r]):
12                r-=1
13            
14            else:
15                l+=1
16
17        return maxarea