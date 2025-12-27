# Last updated: 12/27/2025, 9:00:42 AM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        
4        #check rows
5        for i in range(9):
6            seen = set()
7            for j in range(9):
8                if board[i][j] in seen:
9                    return False
10                elif board[i][j] == ".":
11                    continue
12                else:
13                    seen.add(board[i][j])
14
15        #check columns
16        for i in range(9):
17            seen = set()
18            for j in range(9):
19                if board[j][i] in seen:
20                    return False
21                elif board[j][i] == ".":
22                    continue
23                else:
24                    seen.add(board[j][i])
25
26        #check 3x3
27        for k in range(9):
28            l =(k % 3)*3
29            r = (k // 3)*3
30            seen = set()
31            
32            for i in range(r, r+3):
33                for j in range(l, l+3):
34                    if board[i][j] in seen:
35                        return False
36                    elif board[i][j] == ".":
37                        continue
38                    else:
39                        seen.add(board[i][j])
40        return True