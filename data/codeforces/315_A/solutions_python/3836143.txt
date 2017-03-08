'''
4
1 1
2 2
3 3
4 4
'''

n = int(raw_input())
a = [None] * n
b = [None] * n

for i in xrange(n):
    tmp = raw_input().split(' ')
    a[i] = int(tmp[0])
    b[i] = int(tmp[1])



ans = 0

for i in xrange(n):
    flag = 1
    for j in xrange(n):
        if i != j and b[j] == a[i]:
            flag = 0
            break

    ans += flag


print ans

