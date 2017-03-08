import re
n=input()
q=[len(x) for x in map(str.strip,re.split('[\.!?]',raw_input()))][:-1]
c,m,f=[q[0]+1,1,0]
if c > n: f = 1
for i in xrange(1, len(q)):
    if c + len(' ') + q[i] + len('.') > n:
        m += 1
        c = q[i] + len('.')
        if c > n: f = 1
    else:
        if m == 0: m = 1
        c += (len(' ') + q[i] + len('.'))
print [m, 'Impossible'][f]