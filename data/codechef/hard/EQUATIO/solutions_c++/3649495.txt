#include <cstdio>
#include <iostream>

using namespace std;
int work(int n)
{
	int i,ans=1;
	for(i=2;i*i<=n;i++)
	{
		if(n%i==0)
		{
			ans*=2;
			while(n%i==0)	n/=i;
		}
	}
	if(n>1)	ans<<=1;
	return ans;
}
int main()
{
	int test,a,b,c,d,ans;
	scanf("%d",&test);
	while(test--)
	{
		scanf("%d%d%d",&a,&b,&c);
		if(a==0 && c==0)
		{
			if(b==0)	printf("0\n");
			else		printf("-1\n");
			continue;
		}
		ans=0;
		for(d=b+1;a/d+c>=d-b;d++)
		{
			if(a%d==0 && (a/d+c)%(d-b)==0)
				ans+=work((a/d+c)/(d-b));
		}
		printf("%d\n",ans);
	}
	return 0;
}