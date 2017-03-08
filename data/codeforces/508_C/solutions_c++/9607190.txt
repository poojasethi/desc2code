#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	int m, t, r, w, res = -1;
	set<int> C;
	cin >> m >> t >> r;
	if(t < r) while(m--)cin>>w;
	else {
		res = 0;
		while(m--){
			cin >> w;
			while(!C.empty() && *C.begin() <= w){
				C.erase(C.begin());
			}
			while(C.size() < r){
				C.insert(t + w--);
				res++;
			}
		}
	}
	cout << res << endl;
}
