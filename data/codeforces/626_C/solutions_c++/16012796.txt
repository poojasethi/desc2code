#include <bits/stdc++.h>

using namespace std;

int main(){
	int n,m;
	cin >> n >> m;
	int ans=0;
	for(int i=max(2*n,3*m);i<=6*(n+m);++i)
		if(n+m-(i/2-i/6)-(i/3-i/6)<=i/6){
			ans=i;
			break;
		}
	cout << ans;
}