// Standard includes
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>

//Data Structures
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
using namespace std;

#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i)
#define rep(i,n) FOR(i,0,n)
#define INF INT_MAX
#define all(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())
#define pb push_back
#define sz(x) int(x.size())
#define mp make_pair
#define fill(x,v) memset(x,v,sizeof(x))
#define si(n) scanf("%d",&n)
#define pi(n) printf("%d ",n)
#define pil(n) printf("%d\n",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)

typedef pair<int,int> pr;
typedef vector<int> vec;
typedef vector<vec> matrix;
typedef long long LL;
#define mod 1000000007
//pattern finding problem --> use permutation to get the pattern

/*
 give number of perm of 1..n s.t. sum of ajacent numbers is <=n
 */
LL fact[1000004];
void init(){
fact[0]=1;
fact[1]=1;

FOR(i,2,1000001)
	fact[i] = (fact[i-1]*i)%mod;
}

LL pw(LL num,int base){
int c;
LL ans =1;
while(base){
if(base&1)c=1; else c=0;
base/=2;

if(c)ans = (ans*num)%mod;
num= (num*num)%mod;
}
return ans;
}

int main()
{
int n,k,m;
int v,re;
si(re);
init();
rep(v,re)
{
si(n),si(m);
k = 2*n - m;
LL ans =( ((fact[n-k] * pw(n-k+1,(k+1)/2 ))%mod) *pw(n-k,k/2) )%mod;
printf("%lld\n",ans);
}
return 0;
}

