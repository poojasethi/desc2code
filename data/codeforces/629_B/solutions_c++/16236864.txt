#include <bits/stdc++.h>

using namespace std;

const int MaxN=5E3+10;
const int MaxR=400;
pair <int,int> p[MaxN];

int main(){
	int n;
	cin >> n;
	for (int i=0;i<n;++i){
		char c;
		int l,r;
		cin >> c >> l >> r;
		for (int j=l;j<=r;++j)
			if (c=='F')
				++p[j].first;
			else
				++p[j].second;
	}
	int ans=0;
	for (int i=0;i<MaxR;++i)
		ans=max(ans,2*min(p[i].first,p[i].second));
	cout << ans;
}