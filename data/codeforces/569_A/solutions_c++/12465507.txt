#include <stdio.h>
int main()
{
	int t,s,p,cnt=0;
	scanf("%d%d%d",&t,&s,&p);
	while (s<t)
	{
		s*=p;
		cnt++;
	}
	printf("%d",cnt);
	return 0;
}
