/*******************
  Akash Agrawall
  IIIT HYDERABAD
 ***********************/

#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(i= a ; i < b ; ++i)
#define rep(i,n) FOR(i,0,n)
#define INF INT_MAX
#define ALL(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
#define pb push_back
#define sz(x) int(x.size())
#define mp make_pair
#define fill(x,v) memset(x,v,sizeof(x))
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define si(n) scanf("%d",&n)
#define pi(n) printf("%d ",n)
#define pd(n) printf("%lf ",n);
#define pdl(n) printf("%lf\n",n);
#define pin(n) printf("%d\n",n)
#define pln(n) printf("%lld\n",n)
#define pl(n) printf("%lld ",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define scan(v,n) vector<int> v;rep(i,n){ int j;si(j);v.pb(j);}
#define mod (int)(1e9 + 7)
#define ll long long int
#define MAX 100006
#define TRACE

#ifdef TRACE
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)

#endif
#define gc getchar_unlocked
ll modpow(ll a,ll n,ll temp){ll res=1,y=a;while(n>0){if(n&1)res=(res*y)%temp;y=(y*y)%temp;n/=2;}return res%temp;} 
ll left1[MAX],right1[MAX],left2[MAX],right2[MAX],a[MAX];

void scanint(ll &x)
{
	register ll c = gc();
	x = 0;
	ll neg = 0;
	for(;((c<48 || c>57) && c != '-');c = gc());
	if(c=='-') {neg=1;c=gc();}
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
	if(neg) x=-x;
}

int main()
{
	ll max_so_far = 0, max_ending_here = 0,i,t,n,sz,ans,curr_max;
	scanint(t);
	//sl(t);
	while(t--)
	{
		scanint(n);
		rep(i,n)
			scanint(a[i]);
		sz=n;

		max_so_far = a[0], curr_max = a[0];
		left1[0]=max_so_far;
		for (i = 1; i < sz; i++)
		{
			curr_max = max(a[i], curr_max+a[i]);
			max_so_far = max(max_so_far, curr_max);
			left1[i]=max_so_far;
		}

		max_so_far = a[sz-1], curr_max = a[sz-1];
		right2[sz-1]=max_so_far;
		for (i = sz-2; i >=0 ; i--)
		{
			curr_max = max(a[i], curr_max+a[i]);
			max_so_far = max(max_so_far, curr_max);
			right2[i]=max_so_far;
		}

		rep(i,n)
			a[i]=-a[i];
		max_so_far = a[0], curr_max = a[0];
		left2[0]=max_so_far;
		for (i = 1; i < sz; i++)
		{
			curr_max = max(a[i], curr_max+a[i]);
			max_so_far = max(max_so_far, curr_max);
			left2[i]=max_so_far;
		}
		max_so_far = a[sz-1], curr_max = a[sz-1];
		right1[sz-1]=max_so_far;
		for (i = sz-2; i >=0 ; i--)
		{
			curr_max = max(a[i], curr_max+a[i]);
			max_so_far = max(max_so_far, curr_max);
			right1[i]=max_so_far;
		}
		ans=-mod;
		rep(i,sz-1)
		{
			ans=max(ans,left1[i]+right1[i+1]);
			ans=max(ans,left2[i]+right2[i+1]);
		}
		pln(ans);
	}
	return 0;
}













