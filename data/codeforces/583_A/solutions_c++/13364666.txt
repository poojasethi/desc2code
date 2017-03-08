#include<stdio.h>
int main()
{
	int n,a[60][2]={0},x,y,i,j;
	scanf("%d",&n);
	for(i=0;i<n*n;i++)
	{
		scanf("%d %d",&x,&y);
		if(!a[x][0]&&!a[y][1]){
			printf("%d ",i+1);
			a[x][0]=1;
			a[y][1]=1;
		}

	}
	printf("\n");
}