#include <bits/stdc++.h>
using namespace std ;
char s[100005];
char c[6][20]={"lios","liala","etr","etra","initis","inites"};
char n[6]={4,5,3,4,6,6};
int main()
{
	bool flag=true;
	int noun=0,num=0;
	int last=-1;
	while(scanf("%s",s)!=EOF)
	{
		if(flag)
		{
			num++;
			int t=-1;
			int i;
			int len=strlen(s);
			for(i=0;i<6;i++)
			{
				if(len>=n[i] && strcmp(c[i],s+len-n[i])==0)
				{
					t=i;
					break;
				}
			}
			if(t==2 || t==3) 
				noun++;
			if(t==-1 || (last>=0 && t%2!=last%2)||t<last)
			{
				flag=false;
				continue;
			}
			last=t;
		}
	}
	if(flag && (num==1 || noun==1))
	{
		puts("YES");
	}
	else
	{
		puts("NO");
	}
	return 0;
}