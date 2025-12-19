# Last updated: 12/19/2025, 2:52:01 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        chars1 = dict()
4        chars2 = dict()
5        for c in s:
6            if c in chars1:
7                chars1[c] +=1
8            else:
9                chars1[c] = 1
10
11        for c in t:
12            if c in chars2:
13                chars2[c] +=1
14            else:
15                chars2[c] = 1
16        
17        return chars1 == chars2
18        