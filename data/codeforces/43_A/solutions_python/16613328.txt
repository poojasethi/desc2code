# -*- coding: utf-8 -*-
from collections import Counter

n = int(raw_input())

result = []
for i in xrange(n):
    result.append(raw_input())

print(Counter(result).most_common(1)[0][0])
