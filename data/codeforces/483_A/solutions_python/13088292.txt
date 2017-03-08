import fractions

l, r = map(int, raw_input().split())

for a in range(l,r+1):
    for b in range(a+1,r+1):
        if fractions.gcd(a, b) == 1:
            for c in range(b+1,r+1):
		if fractions.gcd(b, c) == 1 and fractions.gcd(a, c) > 1:
		    print a,b,c
		    exit()      
print "-1"
