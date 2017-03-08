#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9+7;
int a[10], **c, n, b, k, x;
int **matmake(){
	int **arr = new int*[x];
	for(int i = 0 ; i < x ; i++){
		arr[i] = new int[x];
		for(int j = 0 ; j < x ; j++)
			arr[i][j] = 0;
	}
	return arr;
}
int **matmul(int **arr){
	int **ans = matmake();
	for(int i = 0 ; i < x ; i++){
		for(int j = 0 ; j < x ; j++){
			for(int k = 0 ; k < x ; k++){
				ans[i][j] = (ans[i][j] + 1LL * arr[i][k] * c[k][j]) % MOD;
			}
		}
	}
	return ans;
}
int **matexpo(int n){
	int **ans;
	ans = matmake();
	for(int i = 0 ; i < x ; i++)
		ans[i][i] = 1;
	while(n){
		if(n & 1)
			ans = matmul(ans);
		n >>= 1;
		c = matmul(c);
	}
	return ans;
}
int main(){
	int **ans, y;
	scanf("%d%d%d%d", &n, &b, &k, &x);
	c = matmake();
	for(int i = 0 ; i < n ; i++){
		scanf("%d", &y);
		a[y]++;
	}
	for(int i = 0 ; i < x ; i++){
		for(int j = 0 ; j < 10 ; j++)
			c[i][(10 * i + j) % x] += a[j];
	}
	ans = matexpo(b);
	printf("%d\n", ans[0][k]);
	return 0;
}