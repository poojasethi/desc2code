// Program question at: http://www.codechef.com/problems/NSIT15
#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int maxio=1000000;
char buf[1000000], *s = buf + maxio;
inline char getc(void) { if(s >= buf + maxio) { fread(buf,sizeof(char),maxio,stdin); s = buf; } return *(s++); }
inline int input() { char t = getc(); int n=1,res=0; while(t!='-' && !isdigit(t)) t=getc(); if(t=='-') { n=-1; t=getc(); } while(isdigit(t)) { res = 10*res + (t&15); t=getc(); } return res*n; }

inline bool f(int n,int l)
{
	while(n!=0)
	{
		if(n%10 == l) return 1;
		n/=10;
	}
	return 0;
}

int main()
{
	int t=input(), ar[t][2];
	for(int i=0;i<t;i++) { ar[i][0] = input(); ar[i][1] = input(); }

	for(int i=0;i<t;i++)
	{
		int &n = ar[i][0], &l = ar[i][1], ans=0;
		for(int i=1;i<=n;i++)
		{
			ans++;
			while(f(ans,l)) ans++;
		}
		printf("%d\n",ans);
	}
	return 0;
}
