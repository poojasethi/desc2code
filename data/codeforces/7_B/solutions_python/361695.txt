n, m = map(int, raw_input().split())
mem = [0] * m
cnt = 1

for i in xrange(n):
    s = raw_input().split()
    if cmp(s[0], 'alloc') == 0:
        size = int(s[1])
        flag = False
        for j in xrange(m - size + 1):
            if not any(mem[j: j + size]):
                print cnt
                mem[j: j + size] = [cnt] * size
                cnt += 1
                flag = True
                break
        if not flag:
            print 'NULL'
    elif cmp(s[0], 'erase') == 0:
        ordinal = int(s[1])
        if ordinal in mem and cmp(ordinal, 0) != 0:
            '''
            # wrong assignment, take no effect
            for j in mem:
                if cmp(j, ordinal) == 0:
                    j = 0
            '''
            mem = [0 if cmp(j, ordinal) == 0 else j for j in mem]
        else:
            print 'ILLEGAL_ERASE_ARGUMENT'
    else:
        '''
        for j in mem:
            if cmp(j, 0) != 0:
                tmp.append(j)
        mem = tmp + [0] * (m - len(tmp))
        '''
        tmp = [j for j in mem if cmp(j, 0) != 0]
        mem = tmp + [0] * (m - len(tmp))
