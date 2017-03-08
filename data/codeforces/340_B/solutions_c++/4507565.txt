#include<cstdio>
struct rec{int x,y;};
rec a[310];
int n,s;
int lm,rm,mm;
int mul(rec a,rec b,rec c){
	return ((b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x));
}
inline int max(int a,int b){
	return (a>b?a:b);
}
inline int abs(int x){
	return (x>0?x:-x);
}
inline int area(rec a,rec b,rec c){
	return abs(a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y));
}
int main(){
	scanf("%d",&n);
	for (int i=1;i<=n;i++) scanf("%d%d",&a[i].x,&a[i].y);
	mm=0;
	for (int i=1;i<n;i++)
		for (int j=i+1;j<=n;j++){
			lm=rm=0;
			for (int k=1;k<=n;k++) if (k!=i && k!=j){
				s=area(a[i],a[j],a[k]);
				if (mul(a[k],a[i],a[j])>0) rm=max(rm,s);else lm=max(lm,s);
			}
			if (lm && rm) mm=max(mm,lm+rm);
		}
	printf("%d",mm/2);
	if (mm&1) printf(".5");
}
