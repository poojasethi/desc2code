#include <cstdio>
#define N 2000011

char s[N],t[N];

int main()
{
	int n,m;
	scanf("%d%s%s",&n,s,t);
	m=n<<1;
	int a=0,b=0,x=0;
	for(int i=0; i<m; i++)
		if(s[i]!=t[i])
		{
			if(s[i]=='1') a++;
			else b++;
		}
		else if(s[i]=='1')
			x++;
	if(x&1)
	{
		if(a>b) puts("First");
		else if(a==b) puts("First");
		else if(a==b-1||a==b-2)
			puts("Draw");
		else puts("Second");
	}
	else
	{
		if(a>b) puts("First");
		else if(a<b)
		{
			if(a==b-1)
				puts("Draw");
			else
				puts("Second");
		}
		else puts("Draw");
	}
	return 0;
}
