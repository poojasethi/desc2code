from math import *
from Queue import *


n = int(raw_input())
l = map(int, raw_input().split())
if n < 3:
    print(0)
else:
    i = 0
    while (i+1 < n) and (l[i] == l[i+1]):
        i += 1
    if i == n - 1:
        print(0)
    else:
        a = i
        if l[a] < l[a+1]:
            i = a+1
            while (i+1 < n) and (l[i] <= l[i+1]):
                i += 1
            if i == n-1:
                print(0)
            else:
                print(3)
                print(str(a+1) + ' ' + str(i+1) + ' ' + str(i+2))
        if l[a] > l[a+1]:
            i = a+1
            while (i+1 < n) and (l[i] >= l[i+1]):
                i += 1
            if i == n-1:
                print(0)
            else:
                print(3)
                print(str(a+1) + ' ' + str(i+1) + ' ' + str(i+2))
