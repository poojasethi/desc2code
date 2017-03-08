import sys
sys.setrecursionlimit(3000)
n = input()
p = [input() - 1 for i in range(n)]
h = [-1] * n

def dfs(i):
    if h[i] == -1:
        if p[i] == -2:
            h[i] = 0
        else:
            h[i] = dfs(p[i]) + 1
    return h[i]

for i in range(n):
    if h[i] == -1:
        dfs(i)

print max([x+1 for x in h])
