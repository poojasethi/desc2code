#if defined(_MSC_VER)
#define _CRT_SECURE_NO_WARNINGS
#include <boost/typeof/typeof.hpp>
#define __typeof BOOST_TYPEOF
#endif
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <numeric>
#include <valarray>
#include <complex>
#include <memory.h>
using namespace std;

const int dr[]={0,-1,0,1,-1,1, 1,-1};
const int dc[]={1,0,-1,0, 1,1,-1,-1};
const double eps=1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef pair<double, double> pdd;
typedef vector<pdd> vpdd;
typedef complex<double> pnt;
typedef vector<pnt> vpnt;
typedef vector<vector<pair<int, long long> > > Graph;

#define fr(i,a,b) for(int i(a),_b(b);i<=_b;++i)
#define frd(i,a,b) for(int i(a),_b(b);i>=_b;--i)
#define rep(i,n) for(int i(0),_n(n);i<_n;++i)
#define reps(i,a) fr(i,0,sz(a)-1)
#define fore(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define maximum(a) (*max_element(all(a)))
#define minimum(a) (*min_element(all(a)))
#define clr(x,a) memset(x,a,sizeof(x))
#define findx(a,x) (find(all(a),x)-a.begin())
#define two(X) (1LL<<(X))
#define contain(S,X) (((S)&two(X))!=0)

template<class T> void print(T const &x) {ostringstream os; os<<x; cout<<os.str()<<endl;}
template<class T> void print(vector<T> const &v) {ostringstream os; for(int i=0; i<v.size(); ++i){if(i)os<<' ';os<<v[i];} cout<<os.str()<<endl;}
template<class T> void print(vector<vector<T> > const &v){ostringstream os; for(int i=0;i<v.size();++i) {for(int j=0;j<v[i].size();++j){if(j)os<<' ';os<<v[i][j];}os<<endl;}cout<<os.str()<<endl;}
template<class T> void print(valarray<T> const &v) {ostringstream os; for(int i=0; i<v.size(); ++i){if(i)os<<' ';os<<v[i];} cout<<os.str()<<endl;}
template<class T> int sz(const T&c){return (int)c.size();}
template<class T> void srt(T&c){std::sort(c.begin(),c.end());}
template<class T> void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> T sqr(T x){return x*x;}
template<class T, class U> T cast (U x) { ostringstream os; os<<x; T res; istringstream is(os.str()); is>>res; return res; }
template<class T> vector<T> split(string s, string x=" ") {vector<T> res; for(int i=0;i<s.size();i++){string a; while(i<(int)s.size()&&x.find(s[i])==string::npos)a+=s[i++]; if(!a.empty())res.push_back(cast<T>(a));} return res;}
template<class T> bool inside(T r,T c,T R, T C){return r>=0 && r<R && c>=0 && c<C;}


#define N 66

int n,k;
int a[N][N];
int len[N];
int mark[N];
int p[N];
ll f[N][N],g[N][N];

void dfs1(int u)
{
	mark[u]=1;
	for(int i=1;i<len[u];i++)
	{
		int v=a[u][i];
		if(!mark[v]) dfs1(v); else p[u]=v;
	}
}

ll ans;
void dfs(int u)
{
	int i,j,q,v;
	for(i=1;i<len[u];i++)
		dfs(a[u][i]);
	for(j=0;j<=k;j++)
	{
		v=0;
		for(i=1;i<len[u];i++)
		{
			int v1=v;
			v=a[u][i];
			ll &res=g[v][j];
			res=g[v1][j];
			for(q=0;q<j;q++)
				res+=f[v][q]*g[v1][min(j,k-1-q)];
		}
		f[u][j]=g[v][j]-(j?g[v][j-1]:0);
		ans+=f[u][j];
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
#endif
	int T;
	for(scanf("%d",&T);T--;)
	{
		scanf("%d%d",&n,&k);
		memset(len,0,4*n+4);
		int i,j,u,v;
		for(u=1;u<=n;u++)
			a[u][len[u]++]=0;
		for(i=1;i<n;i++)
		{
			scanf("%d%d",&u,&v);
			u++;v++;
			a[u][len[u]++]=v;
			a[v][len[v]++]=u;
		}
		memset(mark,0,4*n+4);
		dfs1(1);
		for(u=1;u<=n;u++)
		{
			for(i=j=1;i<len[u];i++)
				if(a[u][i]!=p[u]) a[u][j++]=a[u][i];
			len[u]=j;
		};
		for(j=0;j<=k;j++) g[0][j]=1;
		ans=0;
		dfs(1);
		printf("%lld\n",ans);
	}
	return 0;
}