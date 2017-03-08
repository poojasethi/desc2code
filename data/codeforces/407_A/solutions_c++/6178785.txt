#include <cstdio>
#include <cmath>
int a,b,c,d,e,f[1000010] = {0};
bool flag = 0;
int main(){
	scanf("%d%d",&a,&b);
	for (int i = 0;i <= 1000;i++) f[i * i] = i;
	for (int i = 1;i < a;i++){
		c = a * a - i * i;
		d = i * b / a;
		if (f[c] && i * b % a == 0 && f[c] != d && f[b * b - d * d]){
			e = i;
			flag = 1;
			break;
		}
	}
	if (flag) printf("YES\n%d %d\n%d %d\n%d %d\n",-e,f[c],0,0,f[b * b - d * d],d);else printf("NO\n");
}
