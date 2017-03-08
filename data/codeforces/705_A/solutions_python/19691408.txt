
n = input()

if n == 1:
	ans = "I hate it"
else:

	ans = ""

	joiner = ["I hate that I love "]*(n/2)
	ans += 'that '.join(joiner)
	
	if n%2:
		ans += "that I hate it"
	else:
		ans += "it"
print ans