def kindof(s):
    if s.endswith('lios'):
        return 0
    elif s.endswith('liala'):
        return 3
    elif s.endswith('etr'):
        return 1
    elif s.endswith('etra'):
        return 4
    elif s.endswith('initis'):
        return 2
    elif s.endswith('inites'):
        return 5
    else:
        return 6

def main(l):
    kind = 0
    for i in l:
        if i == 6:
            return 'NO'
        kind |= 2**(i/3)
    if len(l) == 1:
        return 'YES'
    if kind == 3:
        return 'NO'
    id = -1
    for i in xrange(0, len(l)):
        if l[i] % 3 == 1:
            if id == -1:
                id = i
            else:
                return 'NO'
    if id == -1:
        return 'NO'
    for i in xrange(0, id):
        if l[i] % 3 != 0:
            return 'NO'
    for i in xrange(id + 1, len(l)):
        if l[i] % 3 != 2:
            return 'NO'
    return 'YES'

list = map(kindof,raw_input().split())
print main(list)