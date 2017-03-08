n = int(raw_input())

debut = "I hate "
fin = "it"

s = "I hate "
while n > 1:
	s += "that I love "
	n -= 1
	if n <= 1:
		break
	s += "that I hate "
	n -= 1

print s + fin