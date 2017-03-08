n = map(int, raw_input().split())[0]

l = map(int, raw_input().split())

l.sort()

i, j = 0, len(l)-1
ans = 0
avg = sum(l)/len(l)
r = sum(l)%len(l)

for i in range(len(l)):
    if (l[i] > avg):
        if (r > 0):
            ans += l[i] - avg - 1;
            r -= 1;
        else:
            ans += l[i] - avg;

print ans
