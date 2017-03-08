'''
10 11
1 2 3 4 5 6 7 8 9 10
3 2
3 9
2 10
3 1
3 10
1 1 10
2 10
2 10
3 1
3 10
3 9
'''

tmp = raw_input().split(' ')
n = int(tmp[0])
m = int(tmp[1])

tmp = raw_input().split(' ')
A = [int(_) for _ in tmp]
s = 0
for i in xrange(m):
    tmp = raw_input().split(' ')
    if int(tmp[0]) == 1:
        A[int(tmp[1]) - 1] = int(tmp[2]) - s
    elif int(tmp[0]) == 2:
        s += int(tmp[1])
    else:
        print s + A[int(tmp[1]) - 1],
