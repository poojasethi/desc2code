# -*- coding: utf-8 -*-

n = int(raw_input())
a = map(int, raw_input().split())

max_pos = a.index(max(a))
min_pos = a.index(min(a))

print(max(max(max_pos, min_pos), n - 1 - min(max_pos, min_pos)))
