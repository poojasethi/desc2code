# include <stdio.h>

int n,m,l,r,a,b;

int main()
{
	scanf("%d %d",&n,&m);
	
	for(int h=1; h<=n; h++)
	{
		scanf("%d",&l);
		
		if(l < 0)	a++;
		else b++;
	}
	
		
	for(int h=0; h<m; h++)
	{
		scanf("%d %d",&l,&r);
		int to = r-l+1;
		
		if(to%2 == 0  &&  a >= to/2  &&  b >= to/2)	printf("1\n");
		else 	printf("0\n");
	}
}
