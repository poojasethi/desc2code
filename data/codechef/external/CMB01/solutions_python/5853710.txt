t=input()
for i in range(t):
    a,b=raw_input().split()
    print int(str(int(a[::-1]) + int(b[::-1]))[::-1])
