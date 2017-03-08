n = raw_input()
s = raw_input()
a = []
x = 0
y = 0

ans = 0

for start in xrange(len(s)):
    for end in xrange(start + 1, len(s) + 1):
        comm = s[start:end]
        x, y = 0, 0

        for c in comm:
            if c == 'U':
                y += 1
            elif c == 'D':
                y -= 1
            elif c == 'L':
                x -= 1
            elif c == 'R':
                x += 1

        if x == 0 and y == 0:
            ans += 1

print ans
