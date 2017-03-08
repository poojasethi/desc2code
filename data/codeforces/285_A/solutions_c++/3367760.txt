#include <cstdio>

int main()
{
	int n,k;
	scanf("%d%d",&n,&k);
	int m=n;
	for(; k; m--,k--)
		printf("%d ",m);
	for(int i=1; i<=m; i++)
		printf("%d ",i);
	puts("");
	return 0;
}
