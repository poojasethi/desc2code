#include <bits/stdc++.h>

using namespace std;

#define int long long

int C(int n){
	return n*(n-1)*(n-2)*(n-3)*(n-4)/120;
}

int32_t main(){
	int n;
	cin >> n;
	cout << C(n)*C(n)*120;
}