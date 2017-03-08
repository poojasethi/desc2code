#include <bits/stdc++.h>
using namespace std;
typedef long long int lli;
lli fib[55];
int seq[55];
int main() {
	int n, j;
	lli k;
	scanf("%d", &n);
	cin >> k;
	fib[0] = 0;
	fib[1] = 1;
	for(int i = 2 ; i <= (n+1) ; i++)
		fib[i] = fib[i-1] + fib[i-2];
	j = 0;
	while(j < n){
		if(k <= fib[n-j]){
			seq[j] = j+1;
			j++;
		}
		else{
			seq[j] = j+2;
			seq[j+1] = j+1;
			k -= fib[n-j];
			j+=2;
		}
	}
	for(int i = 0 ; i < n ; i++)
		printf("%d ", seq[i]);
	return 0;
}