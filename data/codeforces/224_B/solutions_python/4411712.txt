import sys

inputs = sys.stdin.readline().split()
n = int(inputs[0])
k = int(inputs[1])
inputs = sys.stdin.readline().split()
l = [int(i) for i in inputs]

def process(end):
    counter2 = 0
    s2 = set()
    for j in xrange(end,-1,-1):
        if (l[j] not in s2):
            counter2 += 1
            s2.add(l[j])
            if (counter2 == k):
                print (j+1), (end+1)

if (k > n):
    print -1, -1
    sys.exit()
if (k == 1):
    print 1, 1
    sys.exit()
else:
    counter = 0
    s = set()
    for i in xrange(n):
        if l[i] not in s:
            counter += 1
            s.add(l[i])
            if (counter == k):
                process(i)
                sys.exit()
    print -1, -1
