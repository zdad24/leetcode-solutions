# Last updated: 12/21/2025, 1:02:17 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        buy = 0
4        sell = 1
5        maxprofit, profit = 0, 0
6        while (sell < len(prices)):
7            profit = prices[sell] - prices[buy]
8            maxprofit = max(maxprofit, profit)
9            if (prices[sell] < prices[buy]):
10                buy=sell
11                sell+=1
12            else:
13                sell+=1
14
15        return maxprofit