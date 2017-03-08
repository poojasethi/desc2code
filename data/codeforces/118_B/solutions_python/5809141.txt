a = range(10)
n = input()
for i in a[:n] + a[n::-1]:
    print ' ' * (n - i) * 2 + ' '.join(map(str, a[:i] + a[i::-1]))