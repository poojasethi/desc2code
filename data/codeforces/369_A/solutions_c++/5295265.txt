# include <stdio.h>

int p, b, d, essi;
int D[1009];

int main()
{
	scanf("%d %d %d",&d,&b,&p);
	
	for(int h=0; h<d; h++)
	{
		scanf("%d",&D[h]);
		if(D[h] == 2  &&  p)	p--;
		else 	essi++;
	}
	
	if(essi <= b)	printf("0");
	else 	printf("%d",essi-b);
}
