import sys
s = sys.stdin.readline()
i = s.find('AB')
j = s.find('BA')
if i != -1 and s.find('BA', i + 2) != -1:
    sys.stdout.write('YES\n')
elif j != -1 and s.find('AB', j + 2) != -1:
    sys.stdout.write('YES\n')
else:
    sys.stdout.write('NO\n')
