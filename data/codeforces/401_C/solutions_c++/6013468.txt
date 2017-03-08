#include<cstdio>

int main()
{
	int n,m,p=1,k=0;
	scanf("%d %d",&n,&m);
	if(n>m+1 || n*2+2<m)
	{
		printf("-1");
		return 0;
	}
	
	while(n || m)
	{
		if(!p || (m>n&&k<2))
			--m,p=1,++k;
		else
			--n,p=0,k=0;
		putchar(p+48);
	}
}