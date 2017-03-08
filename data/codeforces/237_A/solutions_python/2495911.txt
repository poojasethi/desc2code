#! /usr/bin/python
N = input()
time = [0]*9999
for i in range(N):   
    x,y = map(int, raw_input().split())
    time[60*x+y] += 1
print max(time)