n,m = map(int, raw_input().split()) # n:0; m:1
if (n-1 <= m) and (m <= ((n-1)*2) + 4):
	if n > m:
		result = "01" * (n-1)
		print result + "0"
	elif n ==m:
		result = "10" *n
		print result
	else:
		result = ""
		if(n*2 > m):
			result = "110" * (m-n)
			result += "10" * (m-((m-n)*2))
		else:
			result = "110" * n
			result += "1" * (m-(n*2))
		print result
else:
	print -1