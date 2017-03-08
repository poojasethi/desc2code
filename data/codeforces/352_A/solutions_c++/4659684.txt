# include <stdio.h>

int bas, nol, n;

int main()
{
	scanf("%d",&n);
	
	for(int h=0; h<n; h++)
	{int a;
		scanf("%d",&a);
		if(a)	bas++;
		else 	nol++;
	}
	
	if(!nol)	{printf("-1");return 0;}
	
	for(int h=0; h<bas/9; h++)
		for(int j=0; j<9; j++)printf("5");
	
	if(bas/9)	for(int h=0; h<nol; h++)	printf("0");
	else 	printf("0");
}
