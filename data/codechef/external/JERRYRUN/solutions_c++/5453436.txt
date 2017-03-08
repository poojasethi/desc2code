#include <bits/stdc++.h>
using namespace std;

#define R(i,a,b) for(int i=a;i<b;i++)
#define RE(i,a,b) for(int i=a;i<=b;i++)
#define RR(i,a,b) for(int i=a;i>b;i--)
#define RRE(i,a,b) for(int i=a;i>=b;i--)
#define F(i,n) for(int i=0;i<n;i++)
#define FE(i,n) for(int i=0;i<=n;i++)
#define FR(i,n) for(int i=n;i>0;i--)
#define FRE(i,n) for(int i=n;i>=0;i--)
#define mp(a,b) make_pair(a,b)
#define pii pair <int, int>
#define pb push_back
#define ft first
#define sd second
#define LL long long
#define gc getchar_unlocked
#define pc putchar_unlocked

inline void get(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

inline void getll(LL &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

int main()
{
	int T;
	get(T);
	for (int __rep = 1; __rep <=T; __rep++)
	{
		LL x1,x2,v1,v2,t;
		getll(x1);	
		getll(x2);	
		getll(v1);	
		getll(v2);

		if (v1 == v2)
		{
			printf("not possible\n");
			continue;
		}

		if (x1 < x2)
			t = (x1-x2)/(v2-v1);
		else
			t = (x1-x2)/(v1-v2);

		if (t<0)
			printf("not possible\n");
		else if (x1 < x2)
			printf("(%lld,0)\n", (x1+(v1*t)));
		else
			printf("(%lld,0)\n", (x1-(v1*t)));
	}
	return 0;
}