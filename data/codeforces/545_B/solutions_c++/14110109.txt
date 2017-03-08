#include <bits/stdc++.h>

using namespace std;

vector <int> v;

int main(){
	string s,t;
	cin >> s >> t;
	for (int i=0;i<s.size();++i)
		if (s[i]!=t[i])
			v.push_back(i);
	if (v.size()%2==1){
		cout << "impossible";
		return 0;
	}
	string p=s;
	for (int i=0;i<v.size()/2;++i)
		p[v[i]]='1'-p[v[i]]+'0';
	cout << p;
}