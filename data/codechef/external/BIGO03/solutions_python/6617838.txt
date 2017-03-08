// Author : Bony Roopchandani
// 

// INCLUDES
#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

// MACROS
#define all(a) a.begin(), a.end()
#define bg begin()
#define en end()
#define ff first
#define in(a) freopen(a, "r", stdin)
#define ll long long
#define mp make_pair
#define nl printf("\n")
#define out(a) freopen(a, "w", stdout)
#define pb push_back
#define pf(a) printf("%d ",a)
#define pfi(a) printf("%d\n",a)
#define pfl(a) printf("%lld\n",(ll)a)
#define pfs(a) printf("%s\n",a)
#define rep(i, n) for(int i=0; i<n; i++)
#define repd(i, a, b) for(int i=a; i>=b; i--)
#define repl(i, n) for(ll i=0; i<n; i++)
#define repld(i, a, b) for(ll i=a; i>=b; i--)
#define replt(i, a, b) for(ll i=a; i<=b; i++)
#define rept(i, a, b) for(int i=a; i<=b; i++)
#define sfi(a) scanf("%d",&a)
#define sfl(a) scanf("%lld",&a)
#define sfs(a) scanf("%s",a)
#define ss second
#define sz size()

// CONSTS
const double EPS = (1e-11);
const double PI = acos(-1.0);
const int INF = 9999999;
const int MOD = (1e9 + 7);

// TYPEDEFS
typedef list < int > LI;
typedef list < ll > LLL;
typedef map < int, bool > MIB;
typedef map < int, int > MII;
typedef map < int, ll > MIL;
typedef map < ll, int > MLI;
typedef pair < int, int > PII;
typedef pair < int, PII > PIII;
typedef pair < int, PIII > PIIII;
typedef pair < int, ll > PIL;
typedef pair < ll, int > PLI;
typedef set < int > SI;
typedef set < ll > SLL;
typedef vector < int > VI;
typedef vector < ll > VLL;
typedef vector < string > VS;

int a, b, c, d, f1, f2, f3;
ll n;

void mul(ll A[5][5], ll B[5][5], int n, int m) {
	ll ret[5][5]={0};
	rep(i, 4) {
		rep(j, m) {
			rep(k, n) {
				ret[i][j]+=((A[i][k]%MOD)*(B[k][j]%MOD));
				ret[i][j]%=MOD;
			}
		}
	}
	memcpy(A, ret, sizeof ret);
}

void modPow(ll M[5][5], int n) {
	ll ret[5][5]={{1, 0, 0, 0}, {0, 1,0, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}};
	while(n>0) {
		if(n&1) {
			mul(ret, M, 4, 4);
		}
		mul(M, M, 4, 4);
		n>>=1;
	}
	memcpy(M, ret, sizeof ret);
}

ll getNth(ll M[5][5], ll A[5][5]) {
	if(n==1) 
		return f1;
	else if(n==2)
		return f2;
	else if(n==3)
		return f3;
	else {
		modPow(M, n-3);
		mul(M, A, 4, 1);
		return M[0][0]%MOD;
	}
}

int main(void) {
	int T; sfi(T);
	while(T--) {
		cin>>a>>b>>c>>d>>f1>>f2>>f3>>n;
		ll M[5][5]={{a, b, c, 1}, {1, 0, 0, 0}, {0, 1, 0, 0}, {0, 0, 0, 1}};
		ll A[5][5]={{f3}, {f2}, {f1}, {d}};
		pfl(getNth(M, A));
	}
	return (0);
}