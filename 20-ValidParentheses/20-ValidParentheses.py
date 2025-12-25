# Last updated: 12/25/2025, 12:11:03 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4
5        for c in s:
6            if c == "(" or c == "[" or c == "{":
7                stack.append(c)
8            else:
9                if len(stack) == 0:
10                    return False
11                elif c==")" and stack[-1] == "(":
12                    stack.pop()
13                elif c=="]" and stack[-1] == "[":
14                    stack.pop()
15                elif c=="}" and stack[-1] == "{":
16                    stack.pop()
17                else:
18                    stack.append(c)
19                    
20        return len(stack) == 0