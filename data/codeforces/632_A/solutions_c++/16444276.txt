#include <bits/stdc++.h>
#define maxn 12000
using namespace std;
string s[100];
int main()
{
	long long sum=0,ans=0;
	int n,p;
	
	scanf("%d%d ",&n,&p);
	for (int i=1;i<=n;i++) cin>>s[i];
	for (int i=n;i;i--)
	{
		if (s[i]=="half") sum=sum*2;
		else sum=sum*2+1;
		ans+=sum;
	}
	printf("%I64d\n",ans*p/2);
	return 0;
}