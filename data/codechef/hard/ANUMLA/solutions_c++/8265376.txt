#include <bits/stdc++.h>
using namespace std;
#define f(i,n) for(int i=0; i<n; i++)
#define getcx getchar//_unlocked
#define pb push_back
#define mp make_pair

typedef long long int lli;
typedef long long int ll;
typedef pair<int,int> pii;

typedef vector<int> vi;
typedef vector<vi> vvi;

int b[1<<15]; //all subset sum till now
int n;

multiset<ll> s;

void solve(){
	scanf("%d",&n);
	ll a;
	s.clear();
	for(int i=0; i< (1<<n); i++){
		scanf("%lld", &a);
		s.insert(a);
	}
	s.erase(s.find(0));
	int blen = 0;
	vector<ll> ans;
	while(!s.empty()){
		ll curr = *(s.begin());
		ans.pb(curr);
		s.erase(s.begin());
		int currLen = blen;
		for(int i=0; i<currLen; i++){
			s.erase(s.find(curr+b[i]));
			b[blen] = curr+b[i];
			blen++;
		}
		b[blen] = curr;
		blen++;
	}
	for(int i=0; i<ans.size(); i++){
		cout << ans[i] << " ";
	}
	cout << endl;
}

int main(){
	int t;
	scanf("%d", &t);
	while(t--)
		solve();
	return 0;
}