import re
s = re.split('[,;]', raw_input())
a, b = [], []
for w in s:
    if re.match(r'^(?:[1-9]\d*|0)$', w):
        a.append(w)
    else:
        b.append(w)
for q in (a,b):
    if len(q) == 0:
        print '-'
    else:
        print '"%s"'%(','.join(q))
