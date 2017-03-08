"""
Nome: Shayenne Moura
NUSP: 8536235
MAC0327 - 2o sem 2015
3a aval
Problema P21 - 187A. Permutations
"""


n = int(raw_input())

first = map(int, raw_input().split())

second = map(int, raw_input().split())


i = j = 0
while i < n and j < n:
    if first[i] == second[j]:
        i += 1
        j += 1
    else:
        j += 1

print n - i
