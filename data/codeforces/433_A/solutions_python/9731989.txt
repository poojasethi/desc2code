n = int(raw_input())
w = map(int, raw_input().split())

soma = 0
for i in w:
	soma += i

if soma % 200 == 0 and (soma != 200 * n or n % 2 == 0):
	print "YES"
else:
	print "NO"
