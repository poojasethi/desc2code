#include <bits/stdc++.h>

#define MAXN 100010

using namespace std;

int N, x, y;
pair<long double, int> t[MAXN];

int main(){

	cin >> N;
	for (int i = 0; i < N; i++){
		cin >> x >> y;
		t[i] = make_pair(atan2(y, x), i);
	}

	sort(t, t + N);
	long double m = 1000, e; int ans1 = 0, ans2 = 0; 
	for (int i = 0; i < N; i++){
		e = t[(i+1)%N].first - t[i].first;
		if (e < 0) e += 2*acos(-1.0);
		if (e < m){
			m = e;
			ans1 = t[i].second;
			ans2 = t[(i+1)%N].second;
		}
	}

	cout << ans1+1 << " " << ans2+1 << endl;
		
}
