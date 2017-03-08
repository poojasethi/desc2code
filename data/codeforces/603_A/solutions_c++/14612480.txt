#include <bits/stdc++.h>

using namespace std;

int main(){
	int n;
	cin >> n;
	string s;
	cin >> s;
	int ans=1;
	for (int i=1;i<s.size();++i)
		if (s[i-1]!=s[i])
			++ans;
	cout << min(ans+2,n);
}