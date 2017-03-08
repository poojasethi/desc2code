#include <bits/stdc++.h>

using namespace std;

long long dearrange(long long n){

	if (n==1){
		return 0;
	}
	if (n==2){
		return 1;
	}

	return (n-1)*(dearrange(n-1) + dearrange(n-2));
}

int main(){

	long long T = 0;
	cin >> T;

	long long x = 0;
	while(T--){
		cin >> x;
		cout << dearrange(x) <<endl;
	}


	return 0;
}