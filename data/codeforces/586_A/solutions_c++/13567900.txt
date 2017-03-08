#include <iostream>

using namespace std;

int a[111];

int main(){
	int n;
	cin >> n;
	int ans=0;
	for (int i=0;i<n;++i){
		cin >> a[i];
		if (a[i]==1)
			++ans;
	}
	for (int i=1;i<n-1;++i)
		if (a[i]==0 && a[i-1]==1 && a[i+1]==1)
			++ans;
	cout << ans;
}