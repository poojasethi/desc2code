from sys import stdin,exit

if __name__ == "__main__":
	t = input()
	while t:
		n = map(int,stdin.readline().split())[0]
		a = sorted(map(int,stdin.readline().split()))
		a_f = a[:n>>1]
		a_s = a[n>>1:]
		#print a_f,a_s
		
		if n & 1:
			for i in xrange(n>>1):
				print a_f[i],a_s[-1-i],
			print a_s[0]
		else:
			for i in xrange(n>>1):
				print a_f[i],a_s[-1-i],
			print



		t-=1