st1=raw_input()
st2=raw_input()
tmp1=st1.count('+')
#print tmp1
tmp2=st1.count('-')
#print tmp2
dist1=tmp1-tmp2
tmp1=st2.count('+')
tmp2=st2.count('-')
dist2=tmp1-tmp2
diff=dist1-dist2
#print diff,dist1,dist2
#+tive
ques=st2.count('?')
#print ques
cnt=0
for i in xrange(pow(2,ques)):
	st=(bin(i)[2:]).zfill(ques)
	tt1=st.count('0')
	tt2=st.count('1')
	#print st,tt1,tt2
	if diff==tt2-tt1:
		cnt+=1
#print cnt
#print ques,diff
if ques==0 and diff==0:
	print 1
else:
	print float(cnt)/(2**ques)
