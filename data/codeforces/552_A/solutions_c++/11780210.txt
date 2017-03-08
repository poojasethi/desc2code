#include<bits/stdc++.h>

using namespace std;

int main(){
	int ans=0,n,a,b,c,d;
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> a >> b >> c >> d;
		ans+=(c-a+1)*(d-b+1);
	}
	cout << ans << endl;
	return 0;
}	
