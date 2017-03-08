debug = False

import sys, math



def out():
    FIN.close()
    FOUT.close()
    sys.exit()

def num(ind):
    i = 0
    k = ind
    while k > 0:
        i += 1
        if not f[i]:
            k -= 1
    return i

def nextlucky(x):
    s = str(x)
    lens = len(s)
    for i in range(lens - 1, -1, -1):
        if s[i] == '4':
            res = s[:i] + '7' + '4' * (lens - i - 1)
            return int(res)
    return int('4' * (lens + 1))


if debug:
    FIN = open('input.txt', 'r')
    FOUT = open('output.txt', 'w')
else:
    FIN = sys.stdin
    FOUT = sys.stdout

n, k = map(int, FIN.readline().split())

fact = [0] * 14
fact[0] = 1
for i in range(1, 14):
    fact[i] = fact[i - 1] * i
if n < 14 and fact[n] < k:
    FOUT.write('-1')
    out()
a = [0] * 14
p = [0] * 14
f = [False] * 14
for i in range(1, 14):
    a[i] = n - 13 + i
ind = 0
for i in range(1, 14):
    j = 1
    while ind < k:
        j += 1
        ind += fact[13 - i]
    ind -= fact[13 - i]
    j -= 1
    p[i] = num(j)
    f[p[i]] = True

lucky = [0] * 2000
lucky[0] = 4
count = 0
while lucky[count] <= n:
    count += 1
    lucky[count] = nextlucky(lucky[count - 1])

ans = 0
ind = count
for i in range(count):
    if lucky[i] < n - 12:
        ans += 1
    else:
      #  ind = i
        break
for i in range(1, 14):
    if (i + n - 13) > 0 and (a[p[i]] > 0):
        if ((i + n - 13) in lucky) and ((a[p[i]]) in lucky):
            ans += 1
    
FOUT.write(str(ans))        
out()

