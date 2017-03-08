n, m = map(int, raw_input().split())
board = []
u, l, d, r = n, m, 0, 0
for i in range(n):
    board.append(raw_input())
    for j in range(m):
        if board[i][j] == '*':
            if d < i: d = i
            if u > i: u = i
            if l > j: l = j
            if r < j: r = j
for i in range(u, d + 1):
    print board[i][l:r + 1]
