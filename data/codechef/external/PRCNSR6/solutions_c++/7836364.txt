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
#define MAX 1000006
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
#define hit 100005
#define gc getchar_unlocked
ll modpow(ll a,ll n,ll temp){ll res=1,y=a;while(n>0){if(n&1)res=(res*y)%temp;y=(y*y)%temp;n/=2;}return res%temp;} 
int bit[MAX],val[MAX],n;
ll ans, ansit[MAX];
struct node
{
	int b,l,r,qit;
};
vector<node> arr;
bool compare(const node &x, const node &y)
{
	if(x.b==y.b)
		return x.r<y.r;
	return x.b<y.b;
}
void update(int i, int val)
{
	while(i<=hit)
	{
		bit[i]+=val;
		i+=(i&(-i));
	}
}
int query(int i)
{
	int cnt=0;
	i=min(i, hit);
	while(i>0)
	{
		cnt+=bit[i];
		i-=(i&(-i));
	}
	return cnt;
}
void initialize_bit()
{
	int i;
	rep(i,n)
	{
		update(val[i],1);
	}
}
int currentL, currentR;
void initial_calculation(int l, int r, int k)
{
	int i,calc;
	for(i=l; i<r; i++)
	{
		calc=query(val[i]+k) - query(val[i]-k-1);
		ans+=calc-1;
	}
	currentL=0;
	currentR=r-1;
}
void inline findans(int l, int r, int k)
{
	int calc;
	while(currentL<l)
	{
		update(val[currentL], -1);
		calc = query(val[currentL]+k) - query(val[currentL]-k-1);
		ans-=calc;
		currentL++;
	}
	while(currentL>l)
	{
		calc=query(val[currentL-1]+k) - query(val[currentL-1]-k-1);
		ans+=calc;
		update(val[currentL-1],1);
		currentL--;
	}
	while(currentR<r)
	{
		calc=query(val[currentR+1]+k) - query(val[currentR+1]-k-1);
		ans+=calc;
		update(val[currentR+1], 1);
		currentR++;
	}
	while(currentR>r)
	{
		update(val[currentR], -1);
		calc=query(val[currentR]+k) - query(val[currentR]-k-1);
		ans-=calc;
		currentR--;
	}
}
void scanll(int &x)
{
	register int c = gc();
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}
int main()
{
	int l,r,calc,q,k,i;
	ans=0;
	si(n);
	si(q);
	si(k);
	calc=sqrt(n);
	rep(i,n)
	{
		si(val[i]);
	}
	initialize_bit();
	initial_calculation(0, n, k);
	ans/=2;
	rep(i,q)
	{
		node temp;
		scanll(l);
		scanll(r);
		temp.b=(l-1)/calc;
		temp.l=l-1;
		temp.r=r-1;
		temp.qit=i;
		arr.pb(temp);
	}
	sort(arr.begin(), arr.end(), compare);
	rep(i,q)
	{
		findans(arr[i].l, arr[i].r, k);
		ansit[arr[i].qit]=ans;
	}
	rep(i,q)
		pln(ansit[i]);
	return 0;
}
