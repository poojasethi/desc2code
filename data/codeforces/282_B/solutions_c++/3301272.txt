#include <cstdio>

int d;

int main()
{
	d=0;
	int n;
	scanf("%d",&n);
	for(int i=0; i<n; i++)
	{
		int x,y;
		scanf("%d%d",&x,&y);
		if(d+x<=500)
		{
			printf("A");
			d+=x;
		}
		else
		{
			printf("G");
			d-=y;
		}
	}
	puts("");
	return 0;
}
