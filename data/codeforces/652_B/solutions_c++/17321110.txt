#include<bits/stdc++.h>
using namespace std;

int n,a[1005];

int main() {
	scanf("%d",&n);
	for (int i=0; i<n; i++) {
		scanf("%d",&a[i]);
	}	
	
	sort(a,a+n);
	
	printf("%d",a[0]);
	for (int i=1; i<=n/2; i++) {
		printf(" %d",a[n-i]);
		if (i != n-i) printf(" %d",a[i]);
	}
	printf("\n");
}
