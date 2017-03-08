
t = raw_input().split(' ')
n = int(t[0])
k = int(t[1])

s = raw_input()

import re
ret = re.findall('#*', s)
m = 0
for i in ret:
    c = len(i)
    if c > m:
        m = c

print "YES" if m < k else "NO"
