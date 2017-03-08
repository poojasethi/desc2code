#include<cstdio>
using namespace std;
long long n,m,a,b,r[11],o,k;
main(){
	scanf("%I64d%I64d",&n,&m);
	for(int i=0;i<m;++i){
		scanf("%lld%lld",&a,&b);
		r[b]+=a;
	}
	for(int i=10;i&&n;--i){
		if(n>r[i])o=r[i];
		else o=n;
		k+=i*o;
		n-=o;
	}
	printf("%I64d",k);
}