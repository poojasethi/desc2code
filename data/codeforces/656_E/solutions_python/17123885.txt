N = int(raw_input())
xrangen=xrange(N)
g=map(lambda x: map(int,raw_input().split()), xrangen)

def update(k,i,j):
    g[i][j]=min(g[i][j],g[i][k]+g[k][j])
map(lambda k: map(lambda i: map(lambda j: update(k,i,j),xrangen),xrangen),xrangen)

print max(map(max,g))