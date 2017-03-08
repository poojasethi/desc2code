#include <stdio.h>
int times[101]={0};
int main()
{
	int n,m;
	scanf("%d%d",&n,&m);
	for(int i=1; i<=m; i++)
	{
		int l,r;
		scanf("%d %d",&l,&r);
		for(int j=l; j<=r; j++)
			times[j]++;
	}
	bool ok=true;
	for(int i=1; i<=n; i++)
		if((!times[i])||(times[i]>1))
		{
			ok=false;
			printf("%d %d",i,times[i]);
			break;
		}
	if(ok)
		printf("OK");
	return 0;
}
