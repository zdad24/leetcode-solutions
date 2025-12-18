# Last updated: 12/18/2025, 2:29:21 PM
1class Solution(object):
2    def containsDuplicate(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        seen = set()
8
9        for num in nums:
10            if num in seen:
11                return True
12            else:
13                seen.add(num)
14        
15        return False