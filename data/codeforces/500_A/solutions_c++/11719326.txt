#include<stdio.h>

int main()
{
	int n,t;
	scanf("%d%d",&n,&t);
	int a[30001];
	int i;
	for(i=1;i<=n-1;i++)scanf("%d",&a[i]);
	i=1;
	while(i<t)i=i+a[i];
	if(i==t)printf("YES");
	else printf("NO");
	return 0;
}