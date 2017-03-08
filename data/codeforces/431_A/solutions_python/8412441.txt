#n = input()
a = map(int, raw_input().split(" "))
s = raw_input()
c = 0
for item in s:
    c += a[int(item)-1]
print c