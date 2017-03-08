#include <cstdio>
using namespace std;
int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	if(m == 3 && (n == 5 || n == 6)) {
		printf("-1\n");
		return 0;
	}
	for(int i = 0; i < m; ++i)
		printf("%d %d\n", i, i * i + 10000000);
	for(int i = 0; i < n - m; ++i)
		printf("%d %d\n", i, -i * i - 10000000); 
	return 0;
}
