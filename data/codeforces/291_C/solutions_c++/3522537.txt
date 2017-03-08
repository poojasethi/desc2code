#include <cstdio>
#include <iostream>
#include <set>
#define N 100101

using namespace std;
typedef long long LL;

LL ip[N];
LL B(int i){ return 1LL<<i; }

set<LL> st;
int n,k;

int ok(LL x)
{
	st.clear();
	for(int i=0; i<n; i++)
	{
		st.insert(x&ip[i]);
	}
	if(st.size()==k) return 1;
	return 0;
}

int main()
{
	scanf("%d%d",&n,&k);
	for(int i=0; i<n; i++)
	{
		int a,b,c,d;
		scanf("%d.%d.%d.%d",&a,&b,&c,&d);
		ip[i]=(a<<24LL)|(b<<16LL)|(c<<8LL)|d;
	}
	LL ret=0;
	int i;
	for(i=31; i>=0; i--)
	{
		ret|=B(i);
		if(ok(ret))
			break;
	}
	if(i>=0)
	{
		printf("%d.%d.%d.%d\n",int(ret>>24),int((ret>>16)&255),int((ret>>8)&255),int(ret&255));
	}
	else
	{
		puts("-1");
	}
	return 0;
}
