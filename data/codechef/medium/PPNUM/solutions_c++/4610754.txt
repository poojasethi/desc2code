#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int len(long long n)
{
	int ctr=0;
	while (n>0)
	{
		ctr=ctr+1;
		n=n/10;
	}
return ctr;
}
 
int main()
{
	int T;
	long long int L,R;
	int len_L,len_R;
	long long int sum,n,a,p;
	scanf("%d",&T);

	while(T--)
	{
		sum=0;
		scanf("%lld %lld",&L,&R);
		len_L=len(L);
		len_R=len(R);
		if (len_L==len_R)
		{
			n=R-L+1;
			sum=(n*(2*L+n-1))/2;
			sum=sum*len_L;
		}
		else
		{
			while (len_L!=len_R)
			{
					p=pow(10,len_L);
					n=p-L;
					sum+=(n*(L+p-1)/2)*len_L;
					L=p;
					len_L=len_L+1;
			}
			n=R-L+1;
			sum+=(n*(L+R)/2)*len_L;
		}
	printf("\n%lld\n",(sum)%1000000007);
	}
}
