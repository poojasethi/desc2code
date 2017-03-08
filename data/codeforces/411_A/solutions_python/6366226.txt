#!/usr/bin/env python
a = raw_input()
ok = 0
ok1 = 0
ok2 = 0
ok3 = 0
a = list(a)
if (len(a) >= 5):
    ok = 1
for i in range(len(a)):
    if ((a[i] >= 'a') & (a[i] <= 'z')):
        ok1 = 1
    if ((a[i] >= 'A') & (a[i] <= 'Z')):
        ok2 = 1
    if ((a[i] >= '0') & (a[i] <= '9')):
        ok3 = 1
if (ok + ok1 + ok2 + ok3  == 4):
    print "Correct"
else:
    print "Too weak" 
