#include<bits/stdc++.h>
using namespace std;

typedef long long LL;
const int maxn = 1e5 + 10;
char s1[maxn],s2[maxn];

void print(char c1,char c2)
{
	for(int i=0;i<26;++i)
	{
		if('a'+i != c1 && 'a'+i != c2)
		{
			putchar('a'+i);
			return;
		}
	}
}	

int main()
{
	//freopen("test.txt","r",stdin);
	int n,t;
	scanf("%d %d",&n,&t);
	scanf("%s %s",s1,s2);
	int cnt = 0;
	for(int i=0;i<n;++i)
	   	if(s1[i]!=s2[i]) ++cnt;
	t = n-t;
	if((cnt/2+(n-cnt)) < t) puts("-1");
	else
	{
		int rem = cnt/2;
		rem = min(rem,t);
		t -= rem;
		rem*=2;
		for(int i=0;i<n;++i)
		{
			if((s1[i] != s2[i]) && rem)
			{
				if(rem&1) putchar(s1[i]);
				else putchar(s2[i]);
				--rem;
				continue;
			}
			if((s1[i] == s2[i]) && t)
			{
				putchar(s1[i]);
				--t;
				continue;
			}
			print(s1[i],s2[i]);
		}
		puts("");
	}
	return 0;
}


