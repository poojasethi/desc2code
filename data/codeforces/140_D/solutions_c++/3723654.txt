#include<cstdio>
#include<algorithm>
using namespace std;

const int N = 100 + 7;
int a[N], n;

int main() {
	scanf("%d", &n);
	for(int i = 0; i < n; ++i) scanf("%d", &a[i]);
	sort(a, a+n);
	int t = 10, penal = 0, c = 0;
	for(int i = 0; t <= 720 && i < n; ++i) {
		t += a[i];
		if(t <= 720) penal += max(0, t - 360), ++c;
	}
	printf("%d %d\n", c, penal);
	return 0;
}
