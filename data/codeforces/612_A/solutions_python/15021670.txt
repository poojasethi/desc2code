import re
n,p,q=map(int,raw_input().split())
s=raw_input()
m=re.match('(.{%d})*(.{%d})*$'%(p,q),s)
if m:
    e = max(0, m.end(1))
    a = re.findall('.'*p,s[:e]) + re.findall('.'*q,s[e:])
    print len(a)
    print '\n'.join(a)
else:
    print -1
