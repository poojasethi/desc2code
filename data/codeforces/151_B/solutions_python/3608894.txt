#!/usr/bin/env python

import sys

def process():
    n, name = sys.stdin.readline().split()
    n = int(n)
    numbers = [''.join(sys.stdin.readline().split()[0].split('-')) for line in range(n)]
    taxi, pizza, girl = 0, 0, 0
    for number in numbers:
        if len(set(number)) == 1:
            taxi += 1
        elif ''.join(sorted(list(number), reverse=True)) == number and len(set(number)) == 6:
            pizza += 1
        else:
            girl += 1
    return (name, taxi, pizza, girl)

n = int(sys.stdin.readline())
record, result = [], []
while(n>0):
    record.append(process())
    n = n-1
for purpose in range(1,4):
    # purpose, 1=taxi, 2=pizza, 3=girl
    maximum = max(record, key = lambda x: x[purpose])[purpose]
    names = [person[0] for person in record if person[purpose] == maximum]
    result.append(', '.join(names))
print 'If you want to call a taxi, you should call: %s.' % result[0]
print 'If you want to order a pizza, you should call: %s.' % result[1]
print 'If you want to go to a cafe with a wonderful girl, you should call: %s.' % result[2]
