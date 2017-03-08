#include<iostream>

using namespace std;

int a[100005];

int main() {
    int n; cin >> n;
	for(int i = 0; i < n; i++) {
		cin >> a[i];
	}
	int i = n-1;
	while(i > 0 && a[i-1] < a[i]) {
		i--;
	}
	cout << i << endl;
}
