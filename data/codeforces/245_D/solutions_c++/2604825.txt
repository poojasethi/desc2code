# include <stdio.h>

int n;
int t[109][109];
int a[109];

int main()
{
	scanf("%d",&n);
	
	for(int h=0; h<n; h++)
		for(int j=0; j<n; j++)
			scanf("%d",&t[h][j]);
	
	for(int h=0; h<n; h++)
		for(int j=0; j<n; j++)
			if(h!=j)
				a[h]=a[h]|t[h][j];
					
	for(int h=0; h<n; h++)
		printf("%d ",a[h]);
		
}
