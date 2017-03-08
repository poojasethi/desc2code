p=10**9+7;

def modpow(x,n):
	if(n==0):
		return 1;
	elif(n%2==0):
		m=modpow(x,n/2);
		return (m*m)%p;
	else:
		m=modpow(x,n/2);
		return (m*m*x)%p;		

def modinv(x):
	return modpow(x,p-2);



inv2=modinv(2);
mods=[1]*31;

mod2s=[1]*31;
for i in range(1,31):
	mods[i]=(mods[i-1]*3)%p;
	mod2s[i]=(mod2s[i-1]*2);

#A:0 indexed array, m:no. of minutes,x:position in array
#Returns the sum upto position x(0 indexed)
def computeSum(A,m,x):
	if(x==-1):
		return 0;
	sum1=0;
	n=len(A)-1;# An extra element at the end
	i=1;
	while((i<=n)and((i*(2**m)-1)<=x)):
		#INV:Sum of indices upto (i-1)*(2^m)-1 has been taken, i.e. the elements before old A[i-1] (exclusive) has been considered
		sum1=(sum1+A[i-1]+(A[i]+A[i-1])*(mods[m]-1)*inv2)%p;
		i=i+1;
	if((i<=n)and ((i-1)*(2**m))<=x):
		sum1=(sum1+A[i-1]+computePartSum(A[i-1],A[i],m,x-mod2s[m]*(i-1)))%p;
	return sum1;

def computePartSum(a,b,m,x):
	if(m==0):
		return 0;
	mid=2**(m-1)	
	if(x<mid):
		return computePartSum(a,(a+b)%p,m-1,x);
	elif(x==mid):
		return (a+b+(a+(a+b))*(mods[m-1]-1)*inv2)%p;
	else:# x>mid
		return 	(a+b+(a+(a+b))*(mods[m-1]-1)*inv2+computePartSum(a+b,b,m-1,x-(mid)))%p;


T=input();
sums=[];
for i in range(T):
	[N,m,x,y]=map(lambda x:int(x),raw_input().split());
	x=x-1;
	y=y-1;
	A=map(lambda x:int(x),raw_input().split());
	A.append(0);
	sums.append((computeSum(A,m,y)-computeSum(A,m,x-1))%p);

for s in sums:
	print(s);