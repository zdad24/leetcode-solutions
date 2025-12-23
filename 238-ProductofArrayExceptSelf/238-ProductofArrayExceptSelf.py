# Last updated: 12/22/2025, 7:43:14 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = set()
4        res = 0
5        l = 0
6
7        for r in range(len(s)):
8            while s[r] in seen:
9                seen.remove(s[l])
10                l+=1
11            seen.add(s[r])
12            res = max(res, r - l +1)
13
14        return res
15