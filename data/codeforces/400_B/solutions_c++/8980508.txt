#include <bits/stdc++.h>
using namespace std;
char a[1111];
int main(){
	int n,m,i,j,mni = 10000,mxj = 0, mx = 0;
	scanf("%d %d",&n,&m);
	set<int>s;
	while(n --){
		scanf("%s",a);
		i = 0;
		j = 0;
		while(a[i] != 'G') i ++;
		while(a[j] != 'S') j ++;
		if(i > j){
			puts("-1");
			return 0;
		}
		s.insert(j - i);
	}
	printf("%d", s.size());
	return 0;
}