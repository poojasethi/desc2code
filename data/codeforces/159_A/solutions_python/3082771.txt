from sys import stdin

(n, d) = [int(x) for x in stdin.readline().strip().split()]


last = dict()

s = set()

for i in range(n):

    (a, b, t) = stdin.readline().strip().split()

    t = int(t)

    for t0 in last.get((b, a), []):
        if 0 < t - t0 <= d:
            s.add(min((a,b), (b,a)))
            break

    if (a, b) not in last:
        last[(a, b)] = []
    
    last[(a, b)].append(t)


print(len(s))

for p in s:
    print(' '.join(p))
