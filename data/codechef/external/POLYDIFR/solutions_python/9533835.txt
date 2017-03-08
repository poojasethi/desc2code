import operator

def getTerm(v, first=False):
	a = v[0]
	p = v[1]
	s = ''
	if a != 0:
		if not first:
			s += ' + '
 
		if p == 0:
			s += str(a)
		else:
			s += str(a) + "x^" + str(p)
 
	return s
 
 
def main():
	i = 0
	t = int(raw_input())
	while i < t:
		n = int(raw_input())
		v = []
		ans = ''
	
		for x in range(0, n):
			m = raw_input().split(' ')
			tup = (int(m[0]) * int(m[1]), int(m[1]) - 1)
			v.append(tup)

		# sort descending
		v = sorted(v,key=lambda x:(-x[1],x[0]))

		fterm = v[0]
		
		if fterm[1] != 0 and fterm[0] != 0:
			ans = str(fterm[0]) + "x^" + str(fterm[1])
		else:
			ans = str(fterm[0])
	
		for j in range(1, n):
			ans += getTerm(v[j])
	
		print ans
	
		i+=1
 
if __name__ == '__main__':
	main()