from collections import Counter 
n,m = map(int,raw_input().split())
f = map(int,raw_input().split())
b = map(int,raw_input().split())
fcnt = Counter(f)
if any(fcnt[bi] == 0 for bi in b):
	print "Impossible"
elif any(fcnt[bi] > 1 for bi in b):
	print "Ambiguity"
else:
	inv ={v:i+1 for i,v in enumerate(f)}
	print "Possible"
	print " ".join(str(inv[bi]) for bi in b)