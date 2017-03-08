#include<cstdio>
int main()
{
	int n,m,each,mod,rem;
	scanf("%d%d",&n,&m);
	each=n/m;
	mod=n%m;
	rem=m-mod;
	while(mod--)
	printf("%d ",each+1);
	while(rem--)
	printf("%d ",each);
	return 0;
	
}