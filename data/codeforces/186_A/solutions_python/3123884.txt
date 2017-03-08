from sys import stdin

a = stdin.readline().strip()
b = stdin.readline().strip()
diff = sum([0 if a[i] == b[i] else 1 for i in range(min(len(a), len(b)))])

print('YES' if sorted(a) == sorted(b) and
      (diff == 2 or diff == 0 and len(set(a)) < len(a)) else 'NO')
