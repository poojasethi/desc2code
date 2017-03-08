N = input()
A = map(int, raw_input().split(" "))
current = 0
for a in A:
    current += a - 1
    print 2-(current)%2
