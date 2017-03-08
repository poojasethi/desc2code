#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
	int n,b,a[105],dr=0,i;
	double per;
	scanf("%d %d",&n,&b);
	
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
		dr+=a[i];
	}
	
	dr=dr+b;
	per=(double)dr/n;

	if(per<*max_element(a,a+n))
	{
		printf("-1\n");
		return 0;
	}
	else
	{
		for(i=0;i<n;++i)
		{
			printf("%lf\n",per-a[i]);
		}
	}
	
	return 0;
}
