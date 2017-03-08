#include <bits/stdc++.h>

using namespace std;

const int MaxN=10+10;
char c[MaxN][MaxN];

int main(){
	int n,m,t,k;
	cin >> n >> m >> t >> k;
	for (int i=0;i<t;++i){
		int x,y;
		cin >> x >> y;
		--x;
		--y;
		c[x][y]='#';
	}
	int ans=0;
	for (int r1=0;r1<n;++r1)
		for (int r2=r1;r2<n;++r2)
			for (int c1=0;c1<m;++c1)
				for (int c2=c1;c2<m;++c2){
					int cnt=0;
					for (int i=r1;i<=r2;++i)
						for (int j=c1;j<=c2;++j)
							cnt+=(c[i][j]=='#');
					ans+=(cnt>=k);
				}
	cout << ans;
}