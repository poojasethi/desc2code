n, m = map(int, raw_input().split())
if n > m+1 or m > 2*n+2:
	ans = -1
elif n == m+1:
	ans = '01' * m + '0'
else:
	ans = '1x0' * n + 'xx'
	ans = ans.replace('x', '1', m-n)
	ans = ans.replace('x', '')
print ans
