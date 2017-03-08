#include <bits/stdc++.h>

using namespace std;

const int MaxN=100+10;
int a[MaxN];

int main(){
	int n,k;
	cin >> n >> k;
	int mx=0,mn=MaxN;
	for (int i=0;i<n;++i){
		cin >> a[i];
		mx=max(mx,a[i]);
		mn=min(mn,a[i]);
	}
	if (mx-mn>k){
		cout << "NO";
		return 0;
	}
	cout << "YES";
	for (int i=0;i<n;++i){
		cout << endl;
		for (int j=0;j<a[i];++j)
			cout << j%k+1 << " ";
	}
}