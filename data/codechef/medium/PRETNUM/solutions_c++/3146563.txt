/* bhupkas */

#include "bits/stdc++.h"

using namespace std;

typedef long long LL;

bool P[1000005];
LL N[1000005];
LL di[1000005];

vector < int > p;

void pre()
{
	memset(P,true,sizeof(P));
	P[1] = P[0] = false;
	for(int i = 2 ; i * i < 1000005 ; i++)
	{
		if(P[i])
		{
			for(int j = i ; j <= 1000005/i ; j++)	P[i*j] = false;
		}
	}
	for(int i = 2 ; i < 1000005 ; i++)	if(P[i])	p.push_back(i);	
}

int main()
{
	pre();
	int t;
	LL l,r;
	scanf("%d",&t);
	int cnt;
	while(t--)
	{
		cnt = 0;
		scanf("%lld %lld",&l,&r);
		for(LL i = l ; i <= r ; i++)	N[i - l] = i , di[i - l] = 1;
		for(int i = 0 ; i < p.size() ; i++)
		{
			int pri = p[i];
			if(pri > r)	break;
			for(LL j = ((l - 1)/pri + 1)*pri ; j <= r ; j += pri)
			{
				LL num = N[j - l];
				cnt = 0;
				while(num % pri == 0)
				{
					cnt++;
					num /= pri;
				}
				di[j - l] *= (cnt + 1);
				N[j - l] = num;
			}	
		}
		for(LL i = l ; i <= r ; i++)	if(N[i -l] != 1)	di[i - l] *= 2;
		cnt = 0;
		for(LL i = l ; i <= r ; i++)	if(P[di[i - l]])	cnt++; 
		printf("%d\n",cnt);
	}
	return 0;
}