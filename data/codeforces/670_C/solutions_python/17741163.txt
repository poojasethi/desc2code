from collections import defaultdict
n=int(raw_input())
arr=list()
d=defaultdict()
d = defaultdict(lambda: 0, d)
arr=raw_input().split(' ')
for i in arr:
	d[i]=d[i]+1
a=int(raw_input())

audio=list()
audio=raw_input().split(' ')

validAns=list()

cm=-1
for x in audio:
	cm=max(cm,d[x])

for i in range(0,a):
	val=int(d[audio[i]])
	if val==cm:
		validAns.append(i)

video=list()
video=raw_input().split(' ')

cm=-1
ans=1
for i in validAns:
	val=int(d[video[i]])
	if val>cm:
		cm=val
		ans=i+1
print ans 