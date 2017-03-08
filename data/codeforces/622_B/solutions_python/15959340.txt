li = map(int,raw_input().split(":"))
a = input()
li[1] = li[1] + a
li[0]+=li[1]/60
li[0] = li[0]%24
li[1] = li[1]%60
ans = ""
minut = ""
hr = ""
# print li
	
# minut = str(li[1])
if(li[0]<10 and li[1]>=10):
	hr="0"+str(li[0])	
	minut=str(li[1])
if(li[0]>=10 and li[1]<10):
	minut="0"+str(li[1])
	hr=str(li[0])	
if(li[0]>=10 and li[1]>=10):
	minut=str(li[1])
	hr=str(li[0])
if(li[0]<10 and li[1]<10):
	minut="0"+str(li[1])
	hr="0"+str(li[0])	
ans=hr+":"+minut	
print ans