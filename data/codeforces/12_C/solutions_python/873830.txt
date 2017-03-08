n, m = map(int, raw_input().split())
cs = sorted( list(map(int, raw_input().split())) )
buy = dict()
for i in range(m):
    nf = raw_input()
    buy[nf] = buy.get(nf, 0) + 1

counts = sorted(list(buy.values()))
maxi = 0
mini = 0
for i in range(len(counts)):
    maxi += cs[-i - 1] * counts[-i - 1]
    mini += cs[i]      * counts[-i - 1]

print("%d %d" % (mini, maxi))