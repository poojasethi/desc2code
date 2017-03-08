# coding =utf-8
n = int(raw_input())
shake = [[] for i in xrange(2*10**5)]
for i, ai in enumerate(map(int, raw_input().split())):
    shake[ai].append(i+1)
ans = []
indiv = 0
while n:
    if not shake[indiv]:
        indiv -= 3
    elif shake[indiv]:
        ans.append(shake[indiv].pop())
        indiv += 1
        n -= 1
    if indiv < 0:
        print "Impossible"
        exit()

print "Possible"
print " ".join(map(str, ans))