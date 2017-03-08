n = int(input())
v = map(int,raw_input().split())
s = [0]*3
for i in range(len(v)):
    s[i%3] += v[i]
if s[0] == max(s):
    print("chest")
elif s[1] == max(s):
    print("biceps")
else:
    print("back")