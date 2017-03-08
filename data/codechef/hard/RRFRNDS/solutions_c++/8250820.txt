#include<bits/stdc++.h>
using namespace std;
#define AIN(a,b,c) assert(a<=b && b<=c)

long long adj[2005][50];
char str[2005];
int main(){
	int n,i,j,k,ans = 0,x,y;
	scanf("%d",&n);
	AIN(1,n,2000);
	for(i = 0;i<n;i++){
		scanf("%s",str);
		for(j = 0;j<n;j++){
			if(str[j]=='0') continue;
			assert(str[j] == '1');
			x = j / 64;
			y = j % 64;
			adj[i][x] |= (1LL<<y);
		}
	}
	int p = (n + 63)/64;
	for(i = 0;i<n;i++){
		for(j = 0;j<n;j++){
			if(i == j)continue;
			x = j/64;
			y = j%64;
			if(adj[i][x] & (1LL<<y) ) continue;

			for(y = 0;y<=p;y++){
				if(adj[i][y] & adj[j][y]) break;
			}
			if(y<=p) ans++;
		}
	}
	printf("%d\n",ans);
	return 0;
}