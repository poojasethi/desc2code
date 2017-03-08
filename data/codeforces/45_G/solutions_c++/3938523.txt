#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
using namespace std;
int i,j,be[7000],cnt,sum,n;
void work(int x){
	cnt++;
	for(int i=n;i>=1;--i)if(x>=i && !be[i]){
		be[i]=cnt;
		x-=i;
	}
}
bool prime(int x){
	for(int i=2;i*i<=x;++i)if(x%i==0)return 0;
	return 1;
}
int main(){
	scanf("%d",&n);
	sum=n*(n+1)/2;
	if(prime(sum))work(sum);
	else{
		if(sum&1 && prime(sum-2)){
			work(2);
			work(sum-2);
		}else {
			if(sum&1)work(3),sum-=3;
			for(i=2;i<=sum;++i)if(prime(i) && prime(sum-i)){
				work(i);
				work(sum-i);
				break;
			}
		}
	}
	for(i=1;i<=n;++i)printf("%d ",be[i]);
}