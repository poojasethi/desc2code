#include<bits/stdc++.h>
using namespace std;

int main() 
{
	int t,n,i,x;
	long long int k,r,l;
	scanf("%d",&t);
	while(t--) 
	{
		r=0;
		l=0;
		scanf("%d%lld",&n,&k);
		for(i=0;i<n;i++) 
		{
			scanf("%d",&x);
			if(x>l)
			 {
				r+=ceil((float)(x-l)/k);
				l+=ceil(((float)(x-l)/k))*k;
			}
			l-=x;
			if(l>0)l--;
		}
		printf("%lld\n",r);
	}
	return 0;
}
