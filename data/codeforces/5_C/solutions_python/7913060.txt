# http://codeforces.com/problemset/problem/5/C


from sys import stdin


best = 0
cnt = 1
s = stdin.readline().strip()
d = [-1] * len(s)
c = [-1] * len(s)
stack = []

for i, e in enumerate(s):
    if e == ')':
        if len(stack) == 0:
            c[i] = -1
            d[i] = -1
        else:
            d[i] = stack[-1]
            c[i] = d[i]
            pos = d[i] - 1
            if pos >= 0 and c[pos] != -1 and s[pos] == ')':
                c[i] = c[d[i] - 1]
            stack.pop()
            rr = i - c[i] + 1
            if rr == best:
                cnt += 1
            if rr > best:
                cnt = 1
                best = rr
    else:
        stack.append(i)

print str(best) + " " + str(cnt)
