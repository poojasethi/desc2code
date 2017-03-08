#include <bits/stdc++.h>

using namespace std;

int main(){
	int n,p,q;
	cin >> n >> p >> q;
	string s;
	cin >> s;
	int t=-1;
	for (int i=0;i<=s.size()/p;++i)
		if ((n-i*p)%q==0){
			t=i;
			break;
		}
	if (t==-1){
		cout << -1;
		return 0;
	}
	cout << t+(n-t*p)/q << endl;
	for (int i=0;i<t;++i)
		cout << s.substr(i*p,p) << endl;
	for (int i=0;i<(n-t*p)/q;++i)
		cout << s.substr(t*p+i*q,q) << endl;
}