import sys

f = sys.stdin
n = f.readline()
a = f.readline().strip().split(' ')
flag = False
ans = 0
t = '1'
for x in a:
    if x == '0':
        t = '0'
        break
    if flag:
        ans += len(x) - 1
    else:
        if x == '1' + '0' * (len(x) - 1):
            ans += len(x) - 1
        else:
            flag = True
            t = x
if t == '0':
    ans = 0
print t + '0' * ans
