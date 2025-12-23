# Last updated: 12/23/2025, 4:08:59 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        count = {}
4        res = 0
5        l = 0
6        for r in range(len(s)):
7            count[s[r]] = 1 + count.get(s[r], 0)
8            while (r - l + 1) - max(count.values()) > k:
9                count[s[l]]-=1
10                l+=1
11            res = max(res, r - l + 1)
12        return res