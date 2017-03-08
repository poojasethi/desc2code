#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int n; cin>>n;
	vector<int> l(n);
	for (int i=0; i<n; i++) cin>>l[i];
	sort(l.begin(), l.end());
	long long a=0, ret=0;
	for (int i=n-2; i>=0; i--) {
		if(l[i+1]-l[i]<2) {
			if(a) ret+=a*l[i], a=0;
			else a=l[i];
			i--;
		}
	}
	cout << ret << endl;
	return 0;
}
