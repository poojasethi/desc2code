#include <stdio.h>
int a[100001];
bool used[100001];
int main()
{
	int n,i,idx=1;
	scanf("%d",&n);
	for (i=1;i<=n;i++)
	{
		scanf("%d",a+i);
		if (a[i]>n||used[a[i]])
			a[i]=-1;
		used[a[i]]=true;
	}
	for (i=1;i<=n;i++)
	{
		if (a[i]==-1)
		{
			while (used[idx])
				idx++;
			a[i]=idx;
			used[idx]=true;
		}
		printf("%d ",a[i]);
	}
	return 0;
}
