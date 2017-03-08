#include <iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <map>
using namespace std;
#define pb push_back
#define X first
#define Y second
#define spa <<" "
#define lin <<endl
#define foreach(i, x) for(__typeof((x).begin()) i = (x).begin(); i != (x).end(); i ++)
#define Say(x) cout << #x << " = " << x << endl
typedef long long ll;
typedef vector <int> vint;
typedef pair <int,int> pii;

const int Maxn = 1000 * 1000 + 4, Inf = 1e9 + 10;
int nq[Maxn],q;
string s;

#define f(x) ((ll)nq[x]*(x-q/2+1) + x-q/2 + (ll)1 - nq[x])

int bs(int n, int a, int b)
{
	if(a == b) return -1;
	if(a + 1 == b)
		if(f(a) == n) return a;
		else return -1;
	int m = (a+b)/2;
	if(f(m) > n) return bs(n,a,m);
	return bs(n,m,b);
}

int main()
{
	ios::sync_with_stdio(false);
	string o="",t="";
	cin >> s;
	int n = s.length();
	while(s[q] == 'H')
		q++;
	if(q == n)
	{
		cout << "Yes";
		return 0;
	}
	for(int i = q; i < n; i++)
	{
		if(s[i]=='Q') nq[i]++;
		if(i) nq[i]+=nq[i-1];
	}
	nq[n] = nq[n-1];
	if(q%2)
	{
		cout << "No";
		return 0;
	}
	int e = bs(n,q,n);
	if(e == -1)
	{
		cout << "No";
			return 0;
	}	
	for(int i = q/2; i<=e; i++)
		t += s[i];
	for(int i = 0; i<t.length(); i++)
		if(t[i]=='H')
			o += 'H';
		else
			o += t;
	if(o==s)
		cout << "Yes";
	else
		cout << "No";
	return 0;
}