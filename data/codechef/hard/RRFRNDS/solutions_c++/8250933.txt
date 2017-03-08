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
 
int ar[2000][63];
 
string graph[2000];
 
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
		int index = 0, ctr = 0, curr = 0;
		for(int j=0; j<n; j++){
			if(graph[i][j] == '1') curr |= (1<<ctr);
			ctr++;
			if(ctr == 32){
				ar[i][index] = curr;
				index++;
				curr = 0, ctr = 0;
			}
		}
		if(ctr > 0)
			ar[i][index] = curr;
	}
	int ans = 0;
	for(int i=0; i<n; i++){
		for(int j = i+1; j < n; j++){
			if(graph[i][j] == '1')
				continue;
			int upper = ceildiv(n, 32);
			for(int k = 0; k < upper; k++){
				if(ar[i][k] & ar[j][k]){
					ans++;
					break;
				}
			}
		}
	}
 
	cout << ans*2 << endl;
	return 0;
} 