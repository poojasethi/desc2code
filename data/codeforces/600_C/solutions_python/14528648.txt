from collections import deque
s=deque(sorted(raw_input()))
pairs, singles = deque(), deque()
while (s):
    x = s.popleft()
    if s and x == s[0]:
        pairs.append(s.popleft())
    else:
        singles.append(x)
ans = []
while len(pairs)*2+len(singles)>1:
    if pairs:
        if len(singles)>1:
            if pairs[0] <= singles[0]:
                n = pairs.popleft()
            else:
                n = singles.popleft(); singles.pop()
        else:
            n = pairs.popleft()
    else:
        n = singles.popleft(); singles.pop()
    ans.append(n)
print ''.join(ans + list(singles) + list(reversed(ans)))
