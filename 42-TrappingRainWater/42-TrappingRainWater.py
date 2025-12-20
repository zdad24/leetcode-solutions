# Last updated: 12/20/2025, 6:13:20 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        leftmaxes = []
4        rightmaxes = []
5        currentmax = 0
6        for num in height:
7          currentmax = max(currentmax, num)
8          leftmaxes.append(currentmax)
9
10        currentmax = 0
11        for num in height[::-1]:
12            currentmax = max(currentmax, num)
13            rightmaxes.append(currentmax)
14        
15        rightmaxes = rightmaxes[::-1]
16        water = 0
17
18        for i in range(len(height)):
19            if min(leftmaxes[i], rightmaxes[i]) - height[i] < 0:
20                continue
21            else:
22                water += (min(leftmaxes[i], rightmaxes[i]) - height[i])
23       
24        return water
25        