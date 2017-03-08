t = input()
labs = {}
for i in range(t):
	inp = raw_input()
	if(inp not in labs):
		labs[inp]=1
	else:
	 	labs[inp] = labs[inp]+1
for key in sorted(labs.iterkeys()):
	print key,labs[key]
