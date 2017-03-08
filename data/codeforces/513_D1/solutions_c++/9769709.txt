#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<iostream>
#include<map>
#include<queue>
using namespace std;

const int maxn=2000010;

int ch[110],fa[110],dir[110];

int dp[110][110];
int dp1[110][110][110];

int cnt;
void out(int n)
{
	if(!n)
		return;
	int beg=++cnt;
	for(int l=0;l<n;l++)if(dp1[beg][l][n-1-l])
	{
		out(l);
		printf("%d ",beg);
		out(n-1-l);
		return ;
	}
}
int main()
{
	int n,i,j,k;
	int c;
	char s[20];

	cin>>n>>c;

	for(i=1;i<=c;i++)
	{
		cin>>fa[i]>>ch[i]>>s;
		if(s[0]=='L')
			dir[i]=1;
		else
			dir[i]=2;
		if(fa[i]>=ch[i])
		{
			puts("IMPOSSIBLE");
			return 0;
		}
	}

	for(i=n;i>=1;i--)
	{
		for(int l=0;l+i<=n;l++)
		{
			for(int r=0;r+l+i<=n;r++)
			{
				int ok=1;

				if(l&&dp[i+1][i+l]==0)
					continue;
				if(r&&dp[i+l+1][i+l+r]==0)
					continue;
				for(j=1;j<=c;j++)if(dir[j]==1&&fa[j]==i)
				{
					if(ch[j]>l+i)
					{
						ok=0;
						break;
					}
				}
				else if(dir[j]==2&&fa[j]==i)
				{
					if(ch[j]<=l+i||ch[j]>l+i+r)
					{
						ok=0;
						break;
					}
				}
				if(!ok)
					continue;
				dp[i][i+l+r]=1;
				dp1[i][l][r]=1;
			}
		}
	}
	if(!dp[1][n])
		puts("IMPOSSIBLE");
	else
	{
		out(n);
		puts("");
	}
}

