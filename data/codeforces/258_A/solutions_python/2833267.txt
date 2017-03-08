s = raw_input()
p = s.find('0')
if p != -1:
    s = s[:p]+s[p+1:]
else:
    s = s[:-1]
print s
