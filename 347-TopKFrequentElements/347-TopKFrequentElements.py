# Last updated: 12/1/2025, 8:26:01 AM
1class Solution(object):
2    def topKFrequent(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: List[int]
7        """
8
9        count = defaultdict(int)
10        answer = []
11
12        #count nums
13        for num in nums:
14            count[num] += 1
15        
16       #sort and switch 
17        freqlist = []
18        for key, value in count.items():
19            freqlist.append((value, key))
20        
21        freqlist.sort(reverse = True)
22
23        for key, value in freqlist:
24            if (k == 0):
25                break
26            answer.append(value)
27            k-=1
28            
29            
30        return answer