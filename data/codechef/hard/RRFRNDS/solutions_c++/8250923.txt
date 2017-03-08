#include <bits/stdc++.h>
using namespace std;
#define f(i,n) for(int i=0; i<n; i++)
#define getcx getchar//_unlocked
#define pb push_back
#define mp make_pair
 
typedef long long int lli;
typedef long long int ll;
typedef pair<int,int> pii;
 
typedef vector<int> vi;
typedef vector<vi> vvi;
 
ll ar[2005][105];
 
string graph[2005];
 
int ceildiv(int x, int y){
	int ret = x/y;
	if(ret*y == x)
		return ret;
	return (ret+1);
}
 
int main(){
	int n;
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> graph[i];
		for(int j=0; j<n; j++){
			if(graph[i][j] == '0') continue;
			ar[i][j/32] |= (1LL<<(j%32));
		}
	}
	int ans = 0;
	int p = (n + 31)/32, k;
	for(int i=0; i<n; i++){
		for(int j = 0; j < n; j++){
			if(i == j)
				continue;
			if((ar[i][j/32] & (1<<(j%32))))
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
 
	cout << ans << endl;
	return 0;
} 