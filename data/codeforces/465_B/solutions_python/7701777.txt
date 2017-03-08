n = int(raw_input())
a = map(int, raw_input().split())
letters = [i for i, e in enumerate(a) if e == 1]

ans = 1 if len(letters) > 0 else 0
for i, e in enumerate(letters):
    if i == 0:
        continue
    if e - 1 == letters[i-1]:
        ans += 1
    else:
        ans += 2

print ans
