from sys import stdin, stdout
(n, k) = [int(x) for x in stdin.readline().strip().split()]
print(sum([(0 if x.count('4')+x.count('7')>k else 1) for x in stdin.readline().strip().split()]))
