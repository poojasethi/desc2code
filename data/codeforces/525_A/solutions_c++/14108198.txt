#include <iostream>

using namespace std;

int t[30];

int main(){
	int n;
	cin >> n;
	string s;
	cin >> s;
	int ans=0;
	for (int i=1;i<s.size();i+=2){
		++t[s[i-1]-'a'];
		if (t[s[i]-'A']==0)
			++ans;
		else
			--t[s[i]-'A'];
	}
	cout << ans;
}