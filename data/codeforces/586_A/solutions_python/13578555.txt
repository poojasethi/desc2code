n = input()
pairs = raw_input()
pairs = pairs.split(' ')

line = ''
for i in pairs:
	if i == '0':
		line += ' '
	else:
		line += '1'


line = line.strip()

ans = 0
flag = 0

for i in line:
	if i == ' ':
		flag += 1
	else:
		if flag <= 1:
			ans += flag
		flag = 0
		ans += 1

print(ans)