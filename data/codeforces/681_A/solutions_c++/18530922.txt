#include <stdio.h>
int main()
{
	int n,a,b,c=0;
	char str[20];
	scanf("%d",&n);
	while(n--)
	{
	    scanf("%s %d %d",str,&a,&b);
		if(a < b && a>= 2400)
			c=1;
	}
	if(c)
		printf("YES");
	else
		printf("NO");
	return 0;
}
