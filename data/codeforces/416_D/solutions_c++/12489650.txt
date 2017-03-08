#include <stdio.h>
long long a[200005];
int main()
{
	int n,i,j,k,ans=0,d;
	scanf("%d",&n);
	for (i=1;i<=n;i++)
		scanf("%I64d",a+i);
	for (k=1;k<=n;)
	{
		ans++;
		i=k;
		while (a[i]==-1)
			i++;
		j=i+1;
		while (a[j]==-1)
			j++;
		if (j>n)
			break;
		if ((a[j]-a[i])%(j-i))
		{
			k=j;
			continue;
		}
		d=(a[j]-a[i])/(j-i);
		if (a[k]!=-1&&a[j]-d*(j-k)!=a[k]||a[j]-d*(long long)(j-k)<=0)
		{
			k=j;
			continue;
		}
		for (k=j+1;a[k]==-1&&a[j]+d*(long long)(k-j)>0||a[k]==a[j]+d*(long long)(k-j)&&a[k]>0;k++);
	}
	printf("%d",ans);
	return 0;
}
