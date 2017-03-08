#include <bits/stdc++.h>

using namespace std;

#define int long long

const int MaxN=40+10;
string s[MaxN];

int32_t main(){
	int n,p;
	cin >> n >> p;
	for (int i=0;i<n;++i)
		cin >> s[i];
	int cnt=0;
	int ans=0;
	for (int i=n-1;i>=0;--i){
		if (s[i]=="halfplus")
			cnt=2*cnt+1;
		else
			cnt*=2;
		ans+=p*cnt/2;
	}
	cout << ans;
}