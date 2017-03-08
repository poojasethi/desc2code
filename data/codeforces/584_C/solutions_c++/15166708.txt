#include <bits/stdc++.h>

using namespace std;

vector <int> same,dif;

int main(){
	int n,t;
	cin >> n >> t;
	string s1,s2;
	cin >> s1 >> s2;
	string ans;
	for (int i=0;i<n;++i)
		if (s1[i]==s2[i]){
			ans+=s1[i];
			same.push_back(i);
		}
		else{
			char c='a';
			while (c==s1[i] || c==s2[i])
				++c;
			ans+=c;
			dif.push_back(i);
		}
	int x=dif.size();
	for (int i=0;i<same.size() && x<t;++i){
		char c='a';
		while (c==s1[same[i]])
			++c;
		ans[same[i]]=c;
		++x;
	}
	for (int i=0;i+1<dif.size() && x>t;i+=2){
		ans[dif[i]]=s1[dif[i]];
		ans[dif[i+1]]=s2[dif[i+1]];
		--x;
	}
	if (x!=t)
		cout << -1;
	else
		cout << ans;
}