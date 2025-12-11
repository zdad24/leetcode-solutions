# Last updated: 12/11/2025, 5:31:35 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        result = []
4        
5        prefix = []
6
7        postfix = []
8        ans = 1
9        for i in range(len(nums)):
10            ans *= nums[i]
11            prefix.append(ans)
12
13        ans = 1
14        for i in range(len(nums)-1, -1, -1):
15            ans *= nums[i]
16            postfix.append(ans)
17
18        postfix = postfix[::-1]
19
20        for i in range(len(nums)):
21            if i == 0:
22                ans = 1 * postfix[i+1]
23                result.append(ans)
24            elif i == len(nums)-1:
25                ans = prefix[i-1] * 1
26                result.append(ans)
27            else:
28                ans = prefix[i-1] * postfix[i+1]
29                result.append(ans)
30        return result
31
32
33 