n = int(raw_input())
for i in range(n, 0, -1):
    if not n % i:
        n = i
        print n,
