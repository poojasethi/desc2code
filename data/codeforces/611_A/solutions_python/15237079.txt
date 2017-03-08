st=raw_input()
week = [52,52,52,52,53,53,52];
month = [31,29,31,30,31,30,31,31,30,31,30,31];
v = st.split();
if v[2] == 'week':
	print week[int(v[0])-1]
	   
else:
  
	
	cn=0;
	for i in month:
		if int(v[0])<=i:
			cn+=1
	print cn
