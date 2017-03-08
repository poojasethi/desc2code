#include <bits/stdc++.h>

using namespace std;

#define int long long

const int MaxN=2E5+10;
map <int,int> mp1,mp2;

int32_t main(){
	int n;
	cin >> n;
	int ans=0;
	for (int i=0;i<n;++i){
		int x,y;
		cin >> x >> y;
		ans+=mp1[x+y];
		ans+=mp2[x-y];
		++mp1[x+y];
		++mp2[x-y];
	}
	cout << ans;
}