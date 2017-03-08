#include <cstdio>

int main()
{
	long long sum=0;
	int n;
	scanf("%d",&n);
	for(int i=1,p;i<=n;i++)
	{
		scanf("%d",&p);
		sum+=p-1;
		if(sum%2==0) printf("2\n");
		else printf("1\n");
	}
}