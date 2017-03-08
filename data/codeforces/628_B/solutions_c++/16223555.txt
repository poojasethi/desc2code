#include <bits/stdc++.h>

using namespace std;

#define int long long

int32_t main(){
	string s;
	cin >> s;
	int ans=0;
	for (int i=0;i<s.size();++i)
		if (s[i]=='0' || s[i]=='4' || s[i]=='8')
			++ans;
	for (int i=1;i<s.size();++i){
		int x=(s[i-1]-'0')*10+(s[i]-'0');
		if (x%4==0)
			ans+=i;
	}
	cout << ans;
}