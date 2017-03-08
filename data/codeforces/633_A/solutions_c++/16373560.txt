#include <bits/stdc++.h>

using namespace std;

int main(){
	int a,b,c;
	cin >> a >> b >> c;
	for (int i=0;i<=c/a;++i)
		if ((c-(a*i))%b==0){
			cout << "YES";
			return 0;
		}
	cout << "NO";
}