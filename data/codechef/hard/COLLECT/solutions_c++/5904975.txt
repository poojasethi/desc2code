#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <cmath>
#include <cstring>
#include <iostream>
#include <stack>
#include <map>
#include <vector>
#include <utility>
#include <set>

#define MOD (1000000007)
#define MAXINT 1e9
#define EPS (1e-9)
#define mp   make_pair
#define pb   push_back
#define pii  pair<int,int> 
#define se   second
#define fi   first
#define ll long long int

using namespace std;

int a[100005],tree[1000006];

ll fact[3000005];
ll mod=3046201;

void init(int node,int l,int r)
{
	if(l==r){
		tree[node]=a[l];return;
	}
	int left=(node<<1);
	int m=(l+r)>>1;
	init(left,l,m);
	init(left+1,m+1,r);
	tree[node]=tree[left]+tree[left+1];
}

int query(int n,int nl,int nr,int ql,int qr)
{
	if(nl>qr || nr<ql)	return 0;
	if(nl>=ql && nr<=qr)	return tree[n];
	int m=(nl+nr)>>1;
	int left=(n<<1);
	int ans=query(left,nl,m,ql,qr);
	ans+=query(left+1,m+1,nr,ql,qr);
	return ans;
}

void update(int n,int nl,int nr,int t,int q)
{
	if(nl==nr)
	{
		if(nl==t)	tree[n]=q;
		return;
	}
	int left=(n<<1);
	int m=(nl+nr)>>1;
	if(t<=m)	update(left,nl,m,t,q);
	else		update(left+1,m+1,nr,t,q);
	tree[n]=tree[left]+tree[left+1];
}

ll power(ll a,ll x)
{
	ll res=1;
	while(x>0)
	{
		if(x&1)	res=(res*a)%mod;
		a=(a*a)%mod;
		x>>=1;
	}
	return res;
}

int main()
{
	int n,l,i,A,B,r,q,sum,k;
	ll ans;
	char s[20];
	scanf("%d",&n);
	for(i=1;i<=n;i++)	scanf("%d",&a[i]);
	fact[1]=1;
	fact[0]=1;
	for(i=2;i<=(n*30);i++)
		fact[i]=(fact[i-1]*i)%mod;
	init(1,1,n);
	scanf("%d",&q);
	while(q--)
	{
		scanf("%s%d%d",s,&l,&r);
		if(s[0]=='c')
		{
			update(1,1,n,l,r);
		}
		else
		{
			sum=query(1,1,n,l,r);
			//cout<<sum<<endl;
			k=(r-l+1);
			A=sum/k;
			B=sum%k;
			ans=(fact[sum]*fact[k])%mod;
			//cout<<ans<<endl;
			ans=(ans*power(fact[A+1],mod-B-1))%mod;
			//cout<<ans<<endl;
			ans=(ans*power(fact[A],mod-k+B-1))%mod;
			ans=(ans*power(fact[B],mod-2))%mod;
			ans=(ans*power(fact[k-B],mod-2))%mod;
			printf("%lld\n",ans);
		}
	}
	return 0;
}