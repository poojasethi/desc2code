import re

def calc(d, t):
    m = re.match("([&]*)([^*]+)([*]*)", t)
    dec = len(m.group(1))
    name = m.group(2)
    inc = len(m.group(3))
    
    x = d[name] if name in d else -10.0e10
    return x+inc-dec

d = {'void':0}
for _ in xrange(int(raw_input())):
    line = raw_input().strip()
    if line.startswith('typedef'):
        _, t, a = line.split()

        x = calc(d, t)
        if x < 0:
            if a in d:
                del d[a]
        else:
            d[a] = x

    if line.startswith('typeof'):
        _, t = line.split()
        x = calc(d, t)
        if x < 0:
            print "errtype"
        else:
            print "void" + "*" * x
