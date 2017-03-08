k,d = [int(x) for x in raw_input().split()]
zero = "0"
if d == 0 and k > 1:
	print("No solution")
else:
	print(str(d) + zero*(k-1))
