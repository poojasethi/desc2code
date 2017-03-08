s = raw_input()
a = {'a': [0,0], 'b':[0,0]}
odd, even, n = 0, 0, len(s)
for i in range(n):
    a[s[i]][i & 1] += 1
    odd += a[s[i]][i & 1]
    even += a[s[i]][(i+1) & 1]
print even, odd



