#!/usr/bin/env python

cnt = [0]*10
num = map(int, raw_input())
repl = raw_input()
for i in repl:
    cnt[int(i)]+=1

if max(repl) <= min(num):
    print ''.join(map(str, num))
c1 = 0
l1 = len(num)
while c1 < l1:
    c2 = 9
    while c2 >num[c1]:
        if cnt[c2]>0:
            num[c1]=c2
            cnt[c2]-=1
        c2-=1
    c1+=1
print ''.join(map(str, num))