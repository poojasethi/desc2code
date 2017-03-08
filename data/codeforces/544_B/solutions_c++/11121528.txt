#include <cstdio>

int n,k;

int main()
{
	scanf("%d %d",&n,&k);
	if(k<= ((n*n)+1)/2)
	{
		printf("YES\n");
		int count=0;
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<n;++j)
			{
				if(count<k && (i+j)%2==0)
				{
					count++;
					printf("L");
				}
				else printf("S");
			}
			printf("\n");
		}
	}
	else 
		printf("NO\n");

	return 0;
}