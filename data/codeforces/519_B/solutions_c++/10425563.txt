#include <bits/stdc++.h>
using namespace std;

int main(){
	int n;
	while( cin >> n ){
		int a[3], tmp;
		for(int i = 0 ; i < 3 ; i++){
			a[i] = 0;
			for(int j = i ; j < n ; j++){
				cin >> tmp;
				a[i] ^= tmp;
			}
		}
		cout << (a[0] ^ a[1]) << endl << (a[1] ^ a[2]) << endl;
	}
}
