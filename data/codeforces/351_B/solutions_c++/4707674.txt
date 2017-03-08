#include <cstdio>
#define N 4000

int p[N];

int main() {
	int n;
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		scanf("%d",&p[i]);
	}
	int c=0;
	for(int i=0; i<n; i++) {
		for(int j=i+1; j<n; j++) {
			if(p[j]<p[i]) {
				c++;
			}
		}
	}
	if(c&1)
		printf("%.6lf\n",1.0*(2*c-1));
	else
		printf("%.6lf\n",1.0*2*c);
}
