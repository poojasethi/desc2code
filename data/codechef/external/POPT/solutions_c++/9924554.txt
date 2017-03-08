#include "bits/stdc++.h"
using namespace std;
const int N = 505;
int t;
int n;
char arr[N][N];
bool can[N][N];
bool done[N];
int ans;
int main(){
	scanf("%d" , &t);
	while(t--){
		scanf("%d" , &n);
		ans = 0;
		memset(done , 0 , sizeof(done));
		for(int i = 1 ; i <= n ; ++i){
			scanf("%s" , arr[i] + 1);
		}
		for(int i = 1 ; i <= n ; ++i){
			bool ok = 1;
			for(int j = 1 ; j <= n ; ++j){
				if(arr[i][j] == '#'){
					ok = 0;
				}
				can[i][j] = ok;
			}
		}
		for(int j = 1 ; j <= n ; ++j){
			bool ok = 1;
			for(int i = n ; i >= 1 ; --i){
				if(arr[i][j] == '#'){
					ok = 0;
				}
				can[i][j] &= ok;
			}
		}
		for(int j = n ; j >= 1 ; --j){
			for(int i = 1 ; i <= n ; ++i){
				if(can[i][j] && !done[i]){
					done[i] = 1;
					++ans;
					break;
				}
			}
		}
		printf("%d\n" , ans);
	}
} 