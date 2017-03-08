#include<cstdio>
#include<algorithm>
int a[102400],n,i,j,p,t,s;
int main(){
	scanf("%d",&n);
	for(i=0;i<n;++i)scanf("%d",a+i);
	std::sort(a,a+n);
	p=*a;t=0;
	for(i=0;i<n;i=j){
		for(j=i+1;a[j]==a[i];++j);
		if(a[i]-p>1)return puts("NO"),0;
		if((s=j-i)>t)p=a[i],t=s-t;else t-=s;
	}
	puts(t?"NO":"YES");
	return 0;
}