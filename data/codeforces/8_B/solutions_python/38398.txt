line = raw_input()
s = set()
cur = (0, 0)
dirs = {'U': (0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
for d in line:
    s.add(cur)
    next = (cur[0] + dirs[d][0], cur[1] + dirs[d][1])
    meet = 0
    for t in dirs.values():
        if (next[0] + t[0], next[1] + t[1]) in s:
            meet += 1
    if meet != 1 or next in s:
        print 'BUG'
        break
    cur = next
else:
    print 'OK'
