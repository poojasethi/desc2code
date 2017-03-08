#include <cstdio>
bool f[10000010] = {0};
int g(int x){
	int a = 0;
	while (x){
		a = a * 10 + x % 10;
		x /= 10;
	}
	return a;
}
int main(){
	int k = 2000000,p = 0,x;
	scanf("%d",&x);
	int i = 2;
	while (i * i <= k){
		while (f[i]) i++;
		for (int j = 2;i * j <= k;j++) f[i * j] = 1;
		i++;
	}
	for (int i = 2;i <= k;i++) if (!f[i] && !f[g(i)] && i != g(i)){
		p++;
		if (p == x){
			printf("%d\n",i);
			return 0;
		}
	}
}
