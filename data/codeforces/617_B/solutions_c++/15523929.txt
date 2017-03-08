#include<cstdio>
long long n,ans=1,zeros=1,t;
bool st;
int main(){
	scanf("%I64d",&n);
	for(int i=1;i<=n;i++){
		scanf("%I64d",&t);
		if(st){
			if(t==1){ans*=zeros;zeros=0;}
			zeros++;
		}else{
			if(t==1)st=1;
		}
	}
	printf("%I64d",st?ans:0);
}
