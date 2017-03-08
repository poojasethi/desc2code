# Author:   Gilberto A. dos Santos
# Website:  http://codeforces.com/contest/412/problem/B

import sys

r = raw_input().split(" ")
k = int(r[0])
n = int(r[1])

numbers = [int(i) for i in raw_input().split(" ")]
numbers.sort(reverse=True)

print numbers[n-1]
