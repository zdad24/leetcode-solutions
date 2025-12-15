# Last updated: 12/15/2025, 11:40:43 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s = s.lower()
4        cleanedchars = []
5        
6        for char in s:
7            if char.isalnum():
8                cleanedchars.append(char)
9        
10        clean = "".join(cleanedchars)
11
12        rev = clean[::-1]
13
14        return clean == rev