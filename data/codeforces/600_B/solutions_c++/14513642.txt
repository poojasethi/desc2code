#include <iostream>
#include <algorithm>
using namespace std;
int a[200005], b[200005];

int main(){
	int n, m;
	cin >> n >> m;
	for (int i=0; i< n; i++)
		cin >> a[i];
	sort(a, a+n);

	for (int i=0; i< m; i++){
		cin >> b[i];
		cout << upper_bound(a, a+n, b[i]) - a << " ";
	}
	return 0;
}
