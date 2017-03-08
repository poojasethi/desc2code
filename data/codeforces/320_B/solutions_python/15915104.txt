i,n=[],range(int(input()))
def dfs(p,g):
    if g[p]==-1:
        g[p]=0
        for v in range(len(i)):
            if i[v][0]<i[p][0]<i[v][1]or i[v][0]<i[p][1]<i[v][1]:
                if not g[p]:g[p]=dfs(v,g)
    return g[p]
for l in n:
    c,a,b=map(int,raw_input().split())
    if c==1:i+=[(a,b)]
    else:print['NO','YES'][dfs(a-1,[1 if j==b-1 else -1 for j in n])]
