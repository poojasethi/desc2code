def ispossible(files):
	if len(files)==1:
		return False
	for i in range(0,len(files)):
		if i==0:
			if len(files[i])<1 or len(files[i])>8:
				return False
		elif i==len(files)-1:
			if len(files[i])<1 or len(files[i])>3:
				return False
		else:
			if len(files[i])<2 or len(files[i])>11:
				return False
	return True

files = raw_input()
files = files.split('.')
result = []
if ispossible(files) == False:
	print 'NO'
else:
	print 'YES'
	for i in range(1,len(files)-1):
		if len(files[i])==11:
			result.append(files[i-1]+'.'+files[i][0:3])
			files[i]=files[i][3:]
		elif len(files[i])==10:
			result.append(files[i-1]+'.'+files[i][0:2])
			files[i]=files[i][2:]
		else:
			result.append(files[i-1]+'.'+files[i][0:1])
			files[i]=files[i][1:]
	result.append(files[len(files)-2]+'.'+files[len(files)-1])

for e in result:
	print e


