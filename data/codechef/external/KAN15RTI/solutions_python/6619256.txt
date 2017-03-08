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

void toBin(ll n, string& b, string& a) {
	while(n>0) {
		if(n&1) {
			b+="1";
		}
		else {
			b+="0";
		}
		n>>=1;
	}
	if(a.sz>b.sz) {
		while(b.sz != a.sz) {
			b+="0";
		}
	}
	else if(b.sz>a.sz) {
		reverse(all(a));
		while(b.sz != a.sz)
			a+="0";
		reverse(all(a));
	}
	reverse(all(b));
}

int main(void) {
	int T; sfi(T);
	string a, b;
	while(T--) {
		cin>>a;
		ll n; sfl(n);
		toBin(n, b, a);
		bool carry=0;
		repd(i, a.sz-1, 0) {
			if(a[i]=='0' and b[i]=='0') {
				if(carry)
					a[i]='1', carry=0;
				else
					a[i]='0';
			}
			else
			if(a[i]=='0' and b[i]=='1') {
				if(carry)
					a[i]='0';
				else
					a[i]='1';
			}
			else
			if(a[i]=='1' and b[i]=='0') {
				if(carry)
					a[i]='0';
				else
					a[i]='1';
			}
			else
			if(a[i]=='1' and b[i]=='1') {
				if(carry)
					a[i]='1';
				else
					a[i]='0', carry=1;
			}
		}
		if(carry) printf("1");
		cout<<a<<endl;
		a.clear(); b.clear();
	}
	return (0);
}