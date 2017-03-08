/*total queries(l,r pairs) can be 2000*2000,,,,,so we calculated that 
and stored them .....then ans in O(1)*/
#include<iostream>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<utility>
#include<sstream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<string>
#include<cctype>
#include<queue>
#include<deque>
#include<stack>
#include<cmath>
#include<ctime>
#include<list>
#include<map>
#include<set>
#define pi (acos(-1.0))
#define Abs(a) (((a)<0) ? (-(a)) :(a) )
#define rep(i,n) for((i)=0;(i)<(n);(i)++)
#define Rep(i,n) for(int i=0;i<(n);i++)
#define Rrep(i,n) for(int i=n-1;i>=0;i--)
#define rrep(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define Pii pair<int,int>
#define PB push_back
#define Size(x) ((int)(x.size()))
using namespace std;
typedef long long mint;
typedef unsigned long long umint;
int a[20005],bit[20005],ans[20005],n;
vector<Pii> v[20005];
vector<int>pos[20005];
inline void add(int val,int idx)
{
    while(idx<=n)
    {
        bit[idx]+=val;
        idx+=((idx)&(-idx));
    }
}
inline int sum(int idx)
{
    int ans=0;
    while(idx)
    {
        ans+=bit[idx];
        idx-=((idx)&(-idx));
    }
    return ans;
}
int main()
{
	//freopen("in.txt","r",stdin);
	int i,j,l,r,k,mx,cnt;
	scanf("%d",&n);
	map<int,int>mp;
	rep(i,n)
	{
	    scanf("%d",&a[i+1]);
	    //mp[a[i]]=0;
	}
	/*i=0;
	for(map<int,int>::iterator it=mp.begin();it!=mp.end();it++)
	{
	    it->second=i++;
	}*/
	//mx=i;
	int q,val;
	scanf("%d",&q);
	rep(i,q)
	{
	    scanf("%d%d",&l,&r);
	    v[r].PB(Pii(l,i));
	}
	for(i=1;i<=n;i++)
	{
	    //cout<<a[i-1]<<endl;
	    //val=mp[a[i-1]];
	    //cout<<val<<endl;
	    /*for(j=val+1;j<mx;j++)
	    {
	        rep(k,pos[j].size())
	        {
	            add(1,pos[j][k]);
	        }
	    }*/
	    //cout<<"ori a "<<sum(i)<<endl;
	    //pos[val].PB(i);
	    cnt=0;
	    for(j=i-1;j;j--)
	    {
            if(a[j]>a[i])
                cnt++;
            bit[j]+=cnt;
            //cout<<i<<" "<<j<<bit[j]<<endl;
	    }
	    rep(j,v[i].size())
	    {
	        ans[v[i][j].second]=bit[v[i][j].first];
	    }
	}
	rep(i,q)
        printf("%d\n",ans[i]);
	return 0;
}