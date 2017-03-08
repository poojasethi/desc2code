testcase = raw_input();
tc  = int(testcase)

while (tc > 0):
	
	flames = "FLAMES"
	#flames[0] = 'X'
	
	name1=list((raw_input()).replace(' ',''))
	name2=list((raw_input()).replace(' ',''))
	
	
	#ht = {}
	
	count =0
	count1 = 0
	
	i=0
	while(i < len(name1)): 
		j=0
		while(j < len(name2)):
			if(name1[i] == name2[j]):
				name2[j] = '0' 
				name1[i] = '0'
				break	
			j +=1 	
		i += 1		
	
	name1 = "".join(name1)
	name2 = "".join(name2)
	
	joined = str(name1+name2).replace('0','')
	count = len(joined)
	
	"""while( i < len(joined)):
		if ht.has_key(joined[i]):
			ht[joined[i]] = ht[joined[i]] + 1 
		else:
			ht[joined[i]] = 1
		i += 1	
	
	count = 0
	for key in ht:
		ht[key] %= 2
		count += ht[key]"""
	
	letters=6
	 	
	while(len(flames) != 1):
		index = count % letters
		if(index == 0):
			flames=flames.replace(flames[len(flames)-1],"")
		else:
			flames=flames.replace(flames[index-1],"")
			flames=flames[index-1:]+flames[:index-1]
		letters -= 1	
	
	if( flames == "F"):
		print "FRIENDS"
	
	if( flames == "L"):
		print "LOVE"
	
	if( flames == "A"):
		print "ADORE"
	
	if( flames == "M"):
		print "MARRIAGE"
	
	if( flames == "E"):
		print "ENEMIES"
	
	if( flames == "S"):
		print "SISTER"
		
	#print ht.keys(),ht.values()	
	#print count
	#print flames
	
	tc -= 1