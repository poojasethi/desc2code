data = raw_input()
ret = int(0)
accu = int(0)
last_one = '-'
for i in range(len(data)):
	if data[i]!=last_one or accu>=5:
		ret+=1
		last_one = data[i]
		accu = 1
	else:
		accu+=1
print ret
