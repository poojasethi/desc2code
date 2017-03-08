#include <stdio.h>
int mask(int n){
	int r=0;
	int m=1;
	while(10<=n/m)
		m*=10;
	while(0<m){
		if(n/m==4||n/m==7){
			r*=10;
			r+=n/m;
		}
		n%=m;
		m/=10;
	}
	return r;
}
int main(){
	int a,b;
	scanf("%d%d",&a,&b);
	int c=a+1;
	while(mask(c)!=b){
		c++;
	}
	printf("%d\n",c);
	return 0;
}

