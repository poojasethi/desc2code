parentheses = raw_input()

stack = []

a = [-1]*1000005
b = [-1]*1000005

biggest_substring = -1
number_of_substrings = -1

for paren in range(len(parentheses)):
	if parentheses[paren]=="(":
		stack.append(paren)
	else:
		if len(stack)==0:
			a[paren] = -1
			b[paren] = -1
		else:
			starting_parentheses = stack.pop()
			a[paren] = starting_parentheses
			if starting_parentheses == 0:
				b[paren] = 0
			else:
				if parentheses[a[paren]-1] == ")" and b[a[paren]-1] != -1:
					b[paren] = b[a[paren]-1]
				else:
					b[paren] = starting_parentheses
	if b[paren] != -1:
		substring_length = (paren-b[paren])+1
		if biggest_substring < substring_length:
			biggest_substring = substring_length
			number_of_substrings = 1
		elif substring_length == biggest_substring:
			number_of_substrings += 1
			
if biggest_substring == -1:
	print "0 1"
else:
	print "%d %d" % (biggest_substring, number_of_substrings)
