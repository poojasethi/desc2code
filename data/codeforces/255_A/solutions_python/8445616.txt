n = raw_input()
a = map(int, raw_input().split())
#exercise = ["chest", "biceps", "back"]
e = [0] * 3

i = 0
for item in a:
    e[i] += item
    i += 1
    if i == 3:
        i = 0
print ["chest", "biceps", "back"][e.index(max(e))]
