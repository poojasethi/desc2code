import sys
s = sys.stdin.readline().strip();
#print (s);
ls = len (s);
ans = -1;
for i in range (1,ls):
	for j in range (i + 1, ls):
		si = s[:i]; lsi = len (si);
		sj = s[i:j]; lsj = len (sj);
		sk = s[j:]; lsk = len (sk);
		if lsi == 0 or lsj == 0 or lsk == 0 or lsi > 7 or lsj > 7 or lsk > 7:
			continue
		if (lsi == 7 and si != '1000000') or (lsj == 7 and sj != '1000000') \
		   or (lsk == 7 and sk != '1000000'):
			continue
		if (lsi != 1 and si[0] == '0') or (lsj != 1 and sj[0] == '0') \
		   or (lsk != 1 and sk[0] == '0'):
			continue
		
		ans = max (ans, int(si) + int(sj) + int(sk));
print (ans);
			
		
