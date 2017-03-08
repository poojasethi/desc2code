s1 = raw_input()
s2 = raw_input()

p1 = s1.count('+')
n1 = len(s1) - p1
p2 = s2.count('+')
n2 = s2.count('-')
n = len(s2) - p2 - n2
m = abs((p1 - n1) - (p2 - n2))


def f(n):
    return 1 if n <= 1 else n * f(n - 1)


def c(n, m):
    return f(n) / (f(m) * f(n - m))


if n < m or (m + n) % 2 == 1:
    print 0.0
else:
    b = (n - m) / 2
    print float(c(n, b)) / (2 ** n)
