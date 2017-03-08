#include <cstdio>
#include <iostream>
#define N 100101

using namespace std;
typedef long long LL;

LL a[N];

struct node{
	int c[2];
}no[N*80];

int top;

inline int B(LL x,int i){ return (x>>i)&1; }

void insert(LL x)
{
	int p=0;
	for(int i=40; i>=0; i--)
	{
		int nb=B(x,i);
		if(no[p].c[nb])
			p=no[p].c[nb];
		else
		{
			no[p].c[nb]=++top;
			p=top;
		}
	}
}

LL query(LL x)
{
	int p=0;
	LL ret=0;
	for(int i=40; i>=0; i--)
	{
		int nb=B(x,i);
		if(nb)
		{
			if(no[p].c[0])
				p=no[p].c[0];
			else
			{
				p=no[p].c[1];
				ret+=1LL<<i;
			}
		}
		else
		{
			if(no[p].c[1])
			{
				p=no[p].c[1];
				ret+=1LL<<i;
			}
			else
				p=no[p].c[0];
		}
	}
	return ret;
}

int main()
{
	int n;
	scanf("%d",&n);
	LL x=0;
	top=0;
	insert(x);
	for(int i=1; i<=n; i++)
	{
		cin>>a[i];
		x^=a[i];
		insert(x);
	}
	LL ans=0;
	for(int i=1; i<=n; i++)
	{
		LL y=query(x);
		ans=max(ans,max(x^y,x));
		x^=a[i];
	}
	LL y=query(x);
	ans=max(ans,max(y^x,x));
	cout<<ans<<endl;
	return 0;
}
