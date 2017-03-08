n = input()
p = [input() - 1 for i in range(n)]

def cal(i):
    h = 0
    while i != -2:
        h += 1
        i = p[i]
    return h

print max(cal(i) for i in range(n))
