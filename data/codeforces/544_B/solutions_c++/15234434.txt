#include <bits/stdc++.h>

using namespace std;

int main(){
	int n,k;
	cin >> n >> k;
	if (k>(n*n+1)/2){
		cout << "NO";
		return 0;
	}
	cout << "YES" << endl;
	int cnt=0;
	for (int i=0;i<n;++i){
		for (int j=0;j<n;++j)
			if (k>0 && j%2==cnt){
				cout << "L";
				--k;
			}
			else
				cout << "S";
		cnt=1-cnt;
		cout << endl;
	}
}