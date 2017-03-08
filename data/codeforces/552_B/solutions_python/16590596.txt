n = raw_input();
pot= len(n)
n=int(n)
sub="1"

for i in range(1,pot):sub+='1'

result = pot*(n+1)-int(sub)
print result