#include <bits/stdc++.h>

using namespace std;

int main(){
	string s,t;
	cin >> s >> t;
	int ans=0;
	int ls=s.size();
	int lt=t.size();
	for (int i=0;i<=ls-lt;++i){
		string str=s.substr(i,lt);
		if (str==t){
			s[i+lt-1]='#';
			++ans;
		}
	}
	cout << ans;
}