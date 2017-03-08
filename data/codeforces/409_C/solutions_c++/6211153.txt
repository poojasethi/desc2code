#include <cstdio>
int a[5] = {1,1,2,7,4},x,ans;
int main(){
	ans = 1e9;
	for (int i = 0;i < 5;i++){
		scanf("%d",&x);
		if (x / a[i] < ans) ans = x / a[i];
	}
	printf("%d\n",ans);
}
