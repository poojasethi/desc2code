#include <cstdio>
#include <algorithm>
#include <cmath>
#define inf 1000000000

using namespace std;

int main() {
	int n;
	scanf("%d",&n);
	int sum=0,ze=0;
	for(int i=0; i<2*n; i++) {
		double x;
		scanf("%lf",&x);
		int y=int(x*1000+0.5)%1000;
		if(y==0) {
			ze++;
		}
		sum+=y;
	}
	int ret=inf;
	for(int i=min(2*n-ze,n); i>=max(n-ze,0); i--) {
		ret=min(ret,abs(i*1000-sum));
	}
	printf("%.3lf\n",ret*0.001);
	return 0;
}
