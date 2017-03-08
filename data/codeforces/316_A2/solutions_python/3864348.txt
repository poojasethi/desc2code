# include <stdio.h>
# include <string.h>
# include <ctype.h>

int n,f,g;

char s[100009];

int ans=1,d[90];

int main()
{
	scanf("%s",s);
	
	n = strlen(s);
	
	for(int h=0; h<n; h++)
	{
		if(isalpha(s[h]))	d[s[h]-64] = 1;
		if(s[h] == '?')		g++;
	}
	
	for(int h=1; h<50; h++)	f+=d[h];
	
	for(int h=10; h>10-f; h--)	ans *= h;
	
	if(isalpha(s[0]))	ans/=10 , ans *= 9;
	
	if(s[0] == '?')	ans *= 9 , g--;
	
	printf("%d",ans);
	
	for(int h=0; h<g; h++)	printf("0");
}
