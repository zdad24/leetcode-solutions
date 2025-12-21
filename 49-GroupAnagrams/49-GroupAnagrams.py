# Last updated: 12/21/2025, 1:36:46 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        
4        result = defaultdict(list)
5        for s in strs:
6            charcount = [0] * 26
7            for c in s:
8                charcount[ord(c) - ord("a")] +=1
9            result[tuple(charcount)].append(s)
10
11        return list(result.values())
12
13