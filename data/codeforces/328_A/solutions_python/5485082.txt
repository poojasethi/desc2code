a0,a1,a2,a3 = map(int,raw_input().split())
#print a0, a1, a2, a3;
flag = 0;
d = a0 - a1;
if a1 - a2 == d and a2 - a3 == d:
	flag = 1;
q = a1*1.0 / a0;
if a1 != 0 and a2 !=0 and a2*1.0 / a1 == q and a3 *1.0/ a2 == q:
	flag = 2;
#print flag;
if flag == 0 or (flag == 2 and q * a3 != int(q*a3)):
	print "42";
elif flag == 1:
	print -1*d + a3;
else:
	print int(q * a3);



