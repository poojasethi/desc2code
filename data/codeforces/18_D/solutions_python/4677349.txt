#!/usr/bin/python

won = dict()
n = int(raw_input())
profit = 0
for i in range(n):
    desc, cap = raw_input().split()
    cap = int(cap)
    if desc[0] == 'w':
        won[cap] = profit + 2 ** cap
    else:
        if cap in won:
            profit = max(profit, won[cap])
print profit
