raw_input()
s = raw_input()
res = ""
while len(s) > 3:
    res += s[:2] + '-'
    s = s[2:]
res += s
print res