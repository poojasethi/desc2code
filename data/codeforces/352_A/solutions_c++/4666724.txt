#include <iostream>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	int n, x, n5 = 0, n0 = 0;
	cin >> n;
	while(n--){
		cin >> x;
		if(x == 0) n0++;
		if(x == 5) n5++;
	}
		
	if(n0 == 0) cout << -1;
	else if(n5 < 9) cout << 0;
	else{
		n5 = n5-n5%9;
		while(n5--) cout << 5;
		while(n0--) cout << 0;
	}
}
