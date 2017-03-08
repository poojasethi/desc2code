input()
A = map(int, raw_input().split())
ans = []
for i in A:
  if i in range(1, 10):
    ans += [i]
    break
for i in A:
  if i in range(10, 100, 10):
    ans += [i]
    break
if len(ans) == 0:
  for i in A:
    if i not in (0, 100):
      ans += [i]
      break
if 100 in A:
  ans += [100]
if 0 in A:
  ans += [0]
print(len(ans))
print(" ".join(map(str,ans)))