par = map(int, raw_input().split(" "))
n, m = par[0], par[1]

#l, r, t, c = [], [], [], []
win = [[float("inf"), 0] for i in range(n)]

for i in range(m):
    par = map(int, raw_input().split(" "))
    #l.append(par[0])
    #r.append(par[1])
    #t.append(par[2])
    #c.append(par[3])

    for j in range(par[0], par[1]+1):
        if win[j-1][0] > par[2]:
            win[j-1] = [par[2], par[3]]

cost = 0
for item in win:
    if item[0] > 0:
        cost += item[1]
    
print cost