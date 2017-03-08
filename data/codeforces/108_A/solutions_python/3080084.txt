from sys import stdin

def test(m):
    h = m // 60
    m %= 60
    return (h % 10 == m // 10 and h // 10 == m % 10)

(hh, mm) = [int(x) for x in stdin.readline().strip().split(':')]

a = hh * 60 + mm

while True:
    a = (a + 1) % (24 * 60)
    if test(a):
        break

print('%02d:%02d' % (a//60, a%60))
