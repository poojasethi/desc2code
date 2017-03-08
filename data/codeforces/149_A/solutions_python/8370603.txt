k = input()
a = map(int, raw_input().split(" "))
a.sort(reverse = True)
i = 0
while k > 0 and i < 12:
    k -= a[i]
    i += 1
if i == 12 and k > 0:
    i = -1
print i
