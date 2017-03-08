__author__ = 'Aphrodite'

a = raw_input()
b = raw_input()

s = sum(p != q for p, q in zip(a, b))

print 'YES' if sorted(a) == sorted(b) and s == 2 else 'NO'