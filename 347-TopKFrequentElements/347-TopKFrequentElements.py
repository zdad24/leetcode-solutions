# Last updated: 12/24/2025, 5:59:53 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        count = defaultdict(int)
4        freq = []
5        res = []
6
7        for num in nums:
8            count[num] = 1 + count.get(num, 0)
9
10        for key, value in count.items():
11            freq.append((value, key))
12
13        freq.sort(reverse = True)
14        for key, value in freq:
15            if k == 0:
16                break
17            res.append(value)
18            k-=1
19    
20        return res
21