# -*- coding: utf-8 -*-
from collections import Counter

cards = map(int, raw_input().split())
c = Counter(cards).most_common(5)

if len(c) == 5:
    print(sum(cards))
    exit(0)

_max = 0
for card, _count in c:
    if _count > 1:
        _max = max(_max, card * min(_count, 3))

print(sum(cards) - _max)
