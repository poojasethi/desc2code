#include<cstdio>
const int N=100005;
int a[N];
bool f[N];
int main(){
	int n,i;
	while(~scanf("%d",&n)){
		for(i=0;i<n;i++)scanf("%d",a+i);
		long long s=a[n-1];
		f[n-1]=1;
		for(i=n-2;i>=0;i--){
			if(s>0)f[i]=0,s-=a[i];
			else f[i]=1,s+=a[i];
		}
		if(s>=0)for(i=0;i<n;i++)if(f[i])putchar('+');else putchar('-');
		else for(i=0;i<n;i++)if(f[i])putchar('-');else putchar('+');
		puts("");
	}
	return 0;
}