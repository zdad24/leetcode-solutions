# Last updated: 12/12/2025, 4:38:02 PM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3
4        # check rows for duplicates
5        for i in range(9):
6            rowseen = set()
7            for j in range(9):
8                num = board[i][j]
9                if num == ".":
10                    continue
11                elif num in rowseen:
12                    return False
13                else:
14                    rowseen.add(num)
15
16        # check columns for duplicates
17        for i in range(9):
18            columnseen = set()
19            for j in range(9):
20                num = board[j][i]
21                if num == ".":
22                    continue
23                elif num in columnseen:
24                    return False
25                else:
26                    columnseen.add(num)
27
28        # check 3x3
29        rows = 0
30
31        for x in range(9):
32            block_row = x // 3  # Try this!
33            block_col = x % 3   # And this!
34    
35            rows = block_row * 3
36            columns = block_col * 3
37
38            blockseen = set()
39            for i in range(rows, rows + 3):
40                for j in range(columns, columns + 3):
41                    num = board[i][j]
42                    if num == ".":
43                        continue
44                    elif num in blockseen:
45                        return False
46                    else:
47                        blockseen.add(num)
48
49        # valid sudoku
50        return True
51