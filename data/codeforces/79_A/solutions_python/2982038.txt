from sys import stdin

(x, y) = [int(buf) for buf in stdin.readline().strip().split()]

k = min(x//2, y//24)

x -= 2 * k
y -= 24 * k

ans = 0
while y >= 2 and x*100 + y*10 >= 220:
    ans = 1 - ans
    if ans == 1:
        y -= 22 - min(x, 2) * 10
        x -= min(x, 2)
    else:
        x -= 2 - min((y-2)//10, 2)
        y -= 2 + min((y-2)//10, 2) * 10

print('Ciel' if ans == 1 else 'Hanako')
