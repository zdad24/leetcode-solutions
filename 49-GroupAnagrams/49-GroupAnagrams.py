# Last updated: 11/30/2025, 5:39:26 PM
1class Solution(object):
2    def groupAnagrams(self, strs):
3        """
4        :type strs: List[str]
5        :rtype: List[List[str]]
6        """
7        result = defaultdict(list)
8
9        for s in strs:
10            count = [0] * 26
11            for c in s:
12                count[ord(c) - ord("a")] +=1
13            result[tuple(count)].append(s)
14
15        return result.values()