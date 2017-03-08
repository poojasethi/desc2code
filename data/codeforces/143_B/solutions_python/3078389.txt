import sys, re

s = sys.stdin.readline().strip()

m = re.match(r'^(\-?)(\d+)(\.?)(\d*)$', s)

s = '$' + format(int(m.group(2)), ',') + '.' + (m.group(4)+'00')[0:2]

if m.group(1) == '-':
    s = '(' + s + ')'

print(s)
