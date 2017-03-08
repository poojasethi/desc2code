#include <cstdio>
#include <cstring>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

#define MX 500005

char s[2*MX];
int f[2*MX], c;
int n, N, M, P;
vector<bool> can(MX);

int main()
{
	int kases; 
	for(scanf("%d",&kases);kases--;)
	{
		scanf(" %s %d %d",s,&M,&P);
		n = strlen(s); N = 2*n;
		for(int i=0;i<n;i++) s[n+i] = s[i];

		for(int i=1;i<n;i++) can[i] = false;
		can[0] = true;

		//kmp:failure-function
		f[0]=f[1]=c=0;
		for(int i=2,j=1;i<=N;i++,j++)
		{
			while(c>0 && s[c]!=s[j]) c=f[c];
			if(s[j]==s[c]) c++;
			f[i] = c;
			if(i>n && c==n) can[i-n] = true;
			if(c==n) c=f[c]; // <<---
		}

		int ans = 0, ind = 0, k;
		
		for(k=0;k<n;k++)
		{
			ind-=M; ans++; if(ind<0) ind+=n; if(can[ind]) break;
			ind-=P; ans++; if(ind<0) ind+=n; if(can[ind]) break;
		}

		if(k==n) ans= -1; // not reached !?!
		printf("%d\n",ans);
	}
	return 0;
}
