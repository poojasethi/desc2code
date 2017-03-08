from sys import stdin, stdout
(n, k) = [int(x) for x in stdin.readline().strip().split()]
print(0 if k > 3*n else 3*n-k)
