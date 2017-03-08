s = raw_input().strip()
m = input()
length = len(s)
a = list(s)
for i in xrange(m):
    l, r, k  = map(int, raw_input().split())
    # For 1 based index
    l = l-1
    r = r-1
    from collections import deque
    items = deque(a[l:r+1])
    items.rotate(k)
    for j in range(l, r+1):
        a[j] = items.popleft()
print "".join(a) 
