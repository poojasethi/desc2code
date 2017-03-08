#!/usr/bin/env python
alpha = '0123456789ABCDEF'
def to_base(num, base):
    global alpha
    m = int(max(num))
    num = int(num)
    res = ''
    while num >0:
        res+=alpha[num % base]
        num/=base
    return res

a, b = raw_input().split(' ')
res = 0
s = int(max(int(max(a)), int(max(b))))+1
for i in range(s, 17):
    res = max(res, len(to_base(str(int(a, i)+int(b,i)),i)[::-1]))
print res