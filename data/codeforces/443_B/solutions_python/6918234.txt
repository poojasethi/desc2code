s = raw_input()
k = int(raw_input())

max_l = len(s) + k if (len(s) + k) % 2 == 0 else len(s) + k - 1
s += 'A'*k

def check(a, b):
    if a == 'A' or b == 'A':
        return True
    else:
        if a == b:
            return True
        else:
            return False

ans = 0
flag = False
for n in xrange(max_l, 0, -2):
    if flag:
        break
    n = n / 2
    for i in xrange(len(s)):
        for j in xrange(i, i+n):
            if j + n >= len(s):
                break
            if not check(s[j], s[j+n]):
                break
        else:
            ans = 2*n
            flag = True
            break

print ans
