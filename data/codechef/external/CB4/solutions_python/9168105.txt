#include<bits/stdc++.h>
#define ll long long int
using namespace std;

ll lazy[400001];
ll tree[400001];
ll a[100001];

ll raise(ll b, ll exp)
{
    ll r=1;
    while(exp)
    {
        if(exp&1)r=(r*b);
        b=(b*b);
        exp>>=1;
    }
    return r;
}

ll mid(ll a,ll b)
{
	return (a+(b-a)/2);
}

ll cst(ll s,ll e,ll i,ll a[])
{
		int m;
		if(s==e)
		{
			tree[i]=a[s];
			return a[s];
		}
		m=mid(s,e);
		tree[i]=(cst(s,m,2*i+1,a)+cst(m+1,e,2*i+2,a));
		return tree[i];
}

ll q_sum(ll s,ll e,ll l,ll r,ll i,ll a[])
{
	ll m;
	if(lazy[i]!=0)
    {
        tree[i]+=(e-s+1)*lazy[i];
        if(s!=e)
        {
            lazy[2*i+1]+=lazy[i];
            lazy[2*i+2]+=lazy[i];
        }
        lazy[i]=0;
    }
    if(r<s||l>e||s>e)return 0;
	if(l<=s&&r>=e)return tree[i];
	m=mid(s,e);
	return (q_sum(s,m,l,r,2*i+1,a)+q_sum(m+1,e,l,r,2*i+2,a));
}

void update(ll s,ll e,ll l,ll r,ll i,ll a[],ll val)
{
	ll m;
	if(lazy[i]!=0)
    {
        tree[i]+=(e-s+1)*lazy[i];
        if(s!=e)
        {
            lazy[2*i+1]+=lazy[i];
            lazy[2*i+2]+=lazy[i];
        }
        lazy[i]=0;
    }
    if(r<s||l>e||s>e)return;
	if(l<=s&&r>=e)
    {
        tree[i]+=(e-s+1)*val;
        if(s!=e)
        {
            lazy[2*i+1]+=val;
            lazy[2*i+2]+=val;
        }
        return;
    }
	m=mid(s,e);
	update(s,m,l,r,2*i+1,a,val);
	update(m+1,e,l,r,2*i+2,a,val);
	tree[i]=tree[2*i+1]+tree[2*i+2];
}

int main()
{
    ios_base::sync_with_stdio(0);
	ll t,n,q,i,c,x,y,v;
    cin>>t;
    while(t--)
    {
        memset(a,0,sizeof(a));
        memset(tree,0,sizeof(tree));
        memset(lazy,0,sizeof(lazy));
        cin>>n>>q;
        cst(0,n-1,0,a);
        while(q--)
        {
            cin>>c;
            if(c==1)
            {
                cin>>x>>y>>v;
                update(0,n-1,x-1,y-1,0,a,v);
            }
            else
            {
                cin>>x>>y;
                cout<<q_sum(0,n-1,x-1,y-1,0,a)<<endl;
            }
        }
    }


	return 0;
}


