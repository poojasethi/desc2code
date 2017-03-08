#include <bits/stdc++.h>
using namespace std;
#define f(i,n) for(int i=0; i<n; i++)
#define getcx getchar//_unlocked
#define pb push_back
#define mp make_pair

typedef long long int lli;
typedef long long ll;
typedef pair<int,int> pii;

typedef vector<int> vi;
typedef vector<vi> vvi;

ll ar[2005][105];

char str[2005];

int main(){
	int n,x,y;
	scanf("%d",&n);
	for(int i=0; i<n; i++){
		scanf("%s",str);
		for(int j=0; j<n; j++){
			if(str[j] == '0') continue;
			x = j/64;
			y = j%64;
			ar[i][x] |= (1LL<<y);
		}
	}
	int ans = 0;
	int p = (n + 63)/64, k;
	for(int i=0; i<n; i++){
		for(int j = 0; j < n; j++){
			if(i == j)
				continue;
			x = j/64;
			y = j%64;
			if((ar[i][x] & (1LL<<y)))
				continue;
			for(k = 0; k <= p; k++){
				if(ar[i][k] & ar[j][k]){
					break;
				}
			}
			if(k<=p)
				ans++;
		}
	}

	printf("%d\n",ans);
	return 0;
}