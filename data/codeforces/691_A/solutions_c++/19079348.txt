#include <iostream>
using namespace std;
int main() {
	int n;
	cin>>n;
	int f=0, tmp;
	for(int i=0; i<n; ++i) {
		cin>>tmp;
		f+=tmp;
	}
	if((n!=1 && f == n-1) || (n==1 && f == 1)) {
		cout<<"YES";
	} else {
		cout<<"NO";
	}
	return 0;
}
