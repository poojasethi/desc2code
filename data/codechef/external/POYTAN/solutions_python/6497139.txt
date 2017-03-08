
/*
2015-03-14 08:39
practice
MAR 15
*/
#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

typedef long long int ll;

#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORS(i,a,n) for(int i = a; i < n; i++)
#define RDARR(a,n) FOR(i,n) cin>>a[i];
#define SOLVE() int t;cin>>t;FOR(tc,t) solve();
#define PB push_back

void solve(){

	int n;
	cin>>n;
	int a[n][n],b[n][n],c[n][n];
	FOR(i,n)
	FOR(j,n)
	cin>>a[i][j];

	FOR(i,n)
	FOR(j,n)
	cin>>b[i][j];

	FOR(i,n){
		FOR(j,n){
			c[i][j]=0;
			FOR(k,n)
			c[i][j]+=a[i][k]*b[k][j];
		}
	}

	FOR(i,n){
		FOR(j,n)
		cout<<c[i][j]<<" ";
		cout<<endl;
	}

}

int main(){ _

	SOLVE()

	return 0;
}
