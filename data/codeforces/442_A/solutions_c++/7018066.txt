#include <iostream>
#include <cstdio>
#include <algorithm>

#define F(i, a, b) for( int i = (a); i < (b); i++ )
#define min(a, b)  (a > b ? b : a)

using namespace std;

int c[6][6], a[15], b[15];

int chg(char c){
	return c == 'R' ? 0 : c=='G' ? 1 : c == 'B' ? 2 : c == 'Y' ? 3 : 4 ;
}

int main(){
	int n;

	char s [5];
	scanf("%d",&n);

	F(i,0,n){
		scanf("%s",s);
		c[chg(s[0])][s[1] - 49]++;
	}

	int ans = 10;
	F(i,0,1<<10){
		int cnt = 0;
		F(j,0,10){
			cnt += a[j] = i>>j & 1;
		}

		fill_n(b,15,0);
		bool ok = true;
		F(j,0,5){
			F(k,0,5){
				if(c[j][k]){
					if(a[j] && a[k+5]);
					else if(a[j])b[j]++;
					else if(a[k+5])b[k+5]++;
					else b[10]++;
				}
			}
		}
		F(j,0,11) if(b[j] > 1) ok = false;
		if(ok) ans = min(ans,cnt);
	}

	cout << ans << endl;

	return 0;
}

