get = raw_input
a, b = get(), get()

from collections import *
ca, cb = Counter(a), Counter(b)

if set(b) - set(a):
    print -1
else:
    print sum((ca & cb).values())
