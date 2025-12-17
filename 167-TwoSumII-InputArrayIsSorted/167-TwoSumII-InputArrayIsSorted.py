# Last updated: 12/17/2025, 4:17:14 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l = 0
4        r = len(numbers)-1
5
6        while (l < r):
7            if (numbers[l] + numbers[r] == target):
8                return [l+1, r+1]
9            elif (numbers[l] + numbers[r] > target):
10                r-=1
11            else:
12                l+=1