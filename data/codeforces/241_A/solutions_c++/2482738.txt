# include <stdio.h>

int n,k,fuel=0,max,pos,san,ans=0;
int t[2][1009];
bool vis[1009];

int main()
{
	scanf("%d %d",&n,&k);
	
	for(int h=0; h<n; h++)
		scanf("%d",&t[0][h]);
		
	for(int h=0; h<n; h++)
		scanf("%d",&t[1][h]);
	
	for(int h=0; h<n; h++)
	{
		if(max<t[1][h])
			max=t[1][h];
		
		fuel+=t[1][h];
		ans+=t[0][h];
		
		while(fuel-t[0][h]<0)
		{
			fuel+=max;
			ans+=k;
		}
		fuel-=t[0][h];
	}
	
	printf("%d",ans);
}
