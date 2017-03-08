s = raw_input()
t = raw_input()

pos = len(s) - 1
n = ''
while pos >= 0:
    if s[pos] == 'z':
        s = s[:pos] + 'a' + s[(pos + 1):]
        pos -= 1
    else:
        n = s[:pos] + chr(ord(s[pos]) + 1) + s[(pos + 1):]
        break

if len(n) == 0 or n == t:
    print 'No such string'
else:
    print n
