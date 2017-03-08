#include <bits/stdc++.h>
using namespace std;

#define g(n) scanf("%d",&n)
// #define g(n) inp(n)
#define gl(n) scanf("%lld", &n)
// #define f(i,n) for(int i=0; i<n; i++)
#define pb push_back
#define mp make_pair
#define fab(i,a,b) for(int i=a; i<=b; i++)
#define test(t) while(t--)
#define getcx getchar//_unlocked

typedef long long int ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< vi > vvi;


bool f(ll A, ll B)
{
	if((A == 1 && B == 1) || (A>1 && B==1))
	{
		return true;
	}

	if(A == 1 && B > 1)
	{
		return false;
	}

	ll g = __gcd(A,B);
	return f(g, B/g);

}

int main()
{
	int t;
	cin >> t;
	ll A,B;

	test(t)
	{
		cin >> A >> B;
		if(f(A,B))
			cout << "Yes" << endl;
		else
			cout << "No" << endl;
	}
}