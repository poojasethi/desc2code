#!/usr/bin/env python

import sys

def encode(s):
    encoded = []
    counter = 0
    exist = False
    for bit in s:
        if bit == '1':
            encoded.append(counter)
            counter = 0
            exist = True
        else:
            counter += 1
    encoded.append(counter)
    if not exist:
        encoded = None
    return encoded

n = int(sys.stdin.readline())
s = sys.stdin.readline().split()[0]
encoded = encode(s)
result = 0
if n == 0 and not encoded:
    result = len(s) * (len(s) + 1) / 2 
elif n == 0:
    for section in encoded:
        result += section * (section + 1) / 2
elif not encoded or n >= len(encoded):
    result = 0
else:
    start, end, length = 0, n, len(encoded)
    while(end < length):
        result += (encoded[start]+1) * (encoded[end]+1)
        start += 1
        end += 1
print result
