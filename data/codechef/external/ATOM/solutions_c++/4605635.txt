#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t, n, k, m, sec;
	scanf("%lld", &t);
	while(t--)
	{
		scanf("%lld%lld%lld", &n, &k, &m);
		sec = -1;
		if(n>=m)
		{
			printf("0\n");
			continue;
		}
		while(n<=m)
		{
			sec+=1;
			m/=k;
		}
		printf("%lld\n", sec);
	}
	return 0;
}

