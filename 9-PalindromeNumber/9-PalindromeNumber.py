# Last updated: 12/2/2025, 1:54:36 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        strx = str(x)
4        strrev = strx[::-1]
5
6        return strx == strrev