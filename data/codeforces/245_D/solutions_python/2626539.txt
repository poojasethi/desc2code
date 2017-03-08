

n = int(raw_input())
a = []
for _ in range(n):
  y = 0
  for x in map(int, raw_input().split()):
    y |= x if x != -1 else 0
  a.append(y)
print(' '.join(map(str, a)))
