#include<bits/stdc++.h>
using namespace std;

string x(string s) {
	int sz=s.size();
	if(sz%2) return s;
	string u=x(s.substr(0,sz/2)), v=x(s.substr(sz/2));
	if(u<v) return u+v;
	else return v+u;
}

int main() {
	string s,t; cin>>s>>t;
	if(x(s)==x(t)) cout << "YES" << endl;
	else cout << "NO" << endl;
	return 0;
}
