# Last updated: 12/14/2025, 8:52:16 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        seen = set(nums)
4        count = 0
5        maxcount = 0
6        for num in seen:
7            if (not num-1 in seen):
8                count = 1
9                current = num
10                while (current+1 in seen):
11                    count+=1
12                    current+=1
13                maxcount = max(maxcount, count)    
14                
15        return maxcount