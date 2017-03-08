#include<bits/stdc++.h>
using namespace std;

int main() {
	int n,m;
	int ai,bi;
	pair<int,int>a[100];
	scanf("%d%d",&n,&m);
	for (int i=0; i<m; i++) {
		scanf("%d%d",&a[i].second,&a[i].first);
	}
	sort(a,a+m);
	int jawab=0;
	int i=m-1;
	while (i>=0 && n>0) {
		int diambil=min(n,a[i].second);
		jawab+=(a[i].first*diambil);
		n-=diambil;
		i--;
	}
	printf("%d\n",jawab);
	
}
