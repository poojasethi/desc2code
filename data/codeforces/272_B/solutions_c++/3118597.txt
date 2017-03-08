#include <bits/stdc++.h>

int main()
{
	int n,k,s,a[32] = {0},i;
	scanf("%d",&n);
	long long int sum = 0;
	for(i = 0;i < n;i++)
	{
		scanf("%d",&k);
		s = 0;
		while(k >0 )
		{
			if(k&1)
				s++;
			k >>= 1;
		}
		a[s]++;
	}
	for(i = 0;i < 32;i++)
	{
		sum+= ((long long)a[i]*(long long)(a[i]-1))/2;
	}
	printf("%I64d",sum);
	return 0;
}
