# include <stdio.h>

int n;
int sx,sy,ex,ey;
char s[100009];

int main()
{
	scanf("%d %d %d %d %d %s",&n,&sx,&sy,&ex,&ey,s);
	
	for(int h=0; h<n; h++)
	{
		if(s[h] == 'E'  &&  ex-sx > 0)	sx++;
		if(s[h] == 'S'  &&  ey-sy < 0)	sy--;
		if(s[h] == 'W'  &&  ex-sx < 0)	sx--;
		if(s[h] == 'N'  &&  ey-sy > 0)	sy++;
		
		if(sx == ex  &&  sy == ey)
		{
			printf("%d",h+1);
			return 0;
		}
	}
	
	printf("-1");
}
