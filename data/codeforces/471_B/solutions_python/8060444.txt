import math

n = int(raw_input())
h = [int(x) for x in raw_input().split()]

total = 1
for a in set(h):
    total *= math.factorial(h.count(a))
if total<3:
    print 'NO'
    exit()

task = sorted((h[i],i) for i in xrange(n))

para = []
for i in xrange(n-1):
    if task[i][0]==task[i+1][0]:
        para.append(i)
print 'YES'
print ' '.join([str(x[1]+1) for x in task])

tmp = task[para[0]]
task[para[0]]=task[para[0]+1]
task[para[0]+1]=tmp

print ' '.join([str(x[1]+1) for x in task])

tmp = task[para[1]]
task[para[1]]=task[para[1]+1]
task[para[1]+1]=tmp

print ' '.join([str(x[1]+1) for x in task])

