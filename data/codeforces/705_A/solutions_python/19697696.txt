n=int(raw_input())
hate="I hate "
love="I love "
mid="that "
end="it"
ans=""
if(n>=1):
	ans+=hate
if(n>=2):
	ans+=mid
for i in xrange(2,n+1):
	if(i&1):
		ans+=hate
	else:
		ans+=love
	if((i+1)<=n):
		ans+=mid
ans+=end
print ans
