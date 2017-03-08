# include <stdio.h>

int n,m;

int main()
{
	scanf("%d %d",&n,&m);
	
	printf("%d\n",n+m-1);
	
	for(int h=0; h<n; h++)	printf("%d 1\n",h+1);
	
	for(int h=2; h<=m; h++)	printf("1 %d\n",h);
}
