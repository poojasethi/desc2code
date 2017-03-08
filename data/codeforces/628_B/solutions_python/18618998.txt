import sys

f = sys.stdin

n = f.readline().strip()
ind = 0
last_ch = '#'
ans = 0
for ch in n:
    ind += 1
    if int(ch) % 4 == 0:
        ans += 1
    if last_ch != '#':
        if int(last_ch + ch) % 4 == 0:
            ans += ind - 1
    last_ch = ch
print(ans)


# 5810438174
# 0101501001


