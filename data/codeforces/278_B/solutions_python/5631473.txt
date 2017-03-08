import sys

def gen(x):
  if (x < 26):
    return chr(ord("a") + x)
  return gen(x / 26 - 1) + gen(x % 26)

arr = []
n = int(sys.stdin.readline())
for i in range(0, n):
  arr.append(sys.stdin.readline().strip())

cnt = 0
while True:
  if not any((gen(cnt) in x for x in arr)):
    break
  cnt += 1

print gen(cnt)
