#include<stdio.h>
#include<stdlib.h>
struct mes
{
	char name[12];
	int a,h;
}peo[3100];
int cmp(const void *x,const void *y)
{
	return ((struct mes *)x)->a-((struct mes *)y)->a;
}
int main()
{
	int n,i,flag=1,p,j;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		scanf("%s%d",peo[i].name,&peo[i].a);
		peo[i].h=0;
	}
	qsort(&peo[1],n,sizeof(struct mes),cmp);
	for(i=1;i<=n;i++)
	{
		if(peo[i].a>=i)	
		{
			flag=0;
			break;
		}
		p=peo[i].h=peo[i].a+1;
		for(j=i-1;j>=1;j--)
			if(peo[j].h>=p)
				peo[j].h++;
	}
	if(flag)
	{
		for(i=1;i<=n;i++)
			printf("%s %d\n",peo[i].name,5000-peo[i].h);
	}
	else
		printf("-1\n");
	return 0;
}