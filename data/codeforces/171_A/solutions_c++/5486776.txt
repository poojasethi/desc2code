#include <cstdio>
int a,b,c = 0;
int main(){
	scanf("%d%d",&a,&b);
	while (b){
		c =  c * 10 + b % 10;
		b /= 10;
	}
	printf("%d\n",a + c);
}
