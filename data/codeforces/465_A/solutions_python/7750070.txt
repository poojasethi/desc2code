n = raw_input()
s = raw_input()
ret = 0
for e in s:
    if e == '0':
        ret += 1
        break
    ret += 1
print ret
