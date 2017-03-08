# include <stdio.h>

int n, D[109][109], sz[109];

int main()
{
	scanf("%d",&n);
	
	for(int h=0; h<n; h++)
	{
		scanf("%d",&sz[h]);
		for(int j=0; j<sz[h]; j++)	scanf("%d",&D[h][j]);
	}
	
	for(int h=0; h<n; h++)
	{
		bool p = 1;
		
		for(int i=0; i<n; i++)
			if(h != i)
			{
				int k = 0;
				for(int j=0; j<sz[h]; j++)
					for(int j1=0; j1<sz[i]; j1++)
						if(D[h][j] == D[i][j1])
							k++;
				
				if(k == sz[i])	p = 0;
			}
		
		if(p)	printf("YES\n");
		else 	printf("NO\n");
	}
}
