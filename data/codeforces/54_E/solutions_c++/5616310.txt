#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
struct pt{
	double x,y;
}a[120000];
int i,n;
double ans;
double dist(pt &a,pt &b){
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}
double det(pt &a,pt &b,pt &c,pt &d){
	return (b.x-a.x)*(d.y-c.y)-(b.y-a.y)*(d.x-c.x);
}
double dot(pt &a,pt &b,pt &c,pt &d){
	return (b.x-a.x)*(d.x-c.x)+(b.y-a.y)*(d.y-c.y);
}
void work(){
	int i,j;
	double sum=0,h,l1,l2,l;
	pt O={0,0},res;
	j=2;
	for(i=1;i<=n;++i){
		while(dot(a[i],a[i+1],a[j+1],a[j])<0){
			sum+=det(O,a[j+1],O,a[j]);
			j++;
		}
		l1=dist(a[i],a[i+1]);
		l2=dist(a[i],a[j]);
		h=det(a[i],a[j],a[i],a[i+1])/l1;
		l=sqrt(l2*l2-h*h);
		res.x=a[i].x+(a[i+1].x-a[i].x)*l/l1;
		res.y=a[i].y+(a[i+1].y-a[i].y)*l/l1;
		ans=min(ans,det(O,a[j],O,res)+det(O,res,O,a[i+1])-sum);
		sum-=det(O,a[i+2],O,a[i+1]);
	}
}
int main(){
	scanf("%d",&n);
	ans=1e18;
	for(i=1;i<=n;++i)scanf("%lf%lf",&a[i].x,&a[i].y),a[i+n]=a[i];
	if(det(a[1],a[2],a[2],a[3])>0)reverse(a+1,a+n+n+1);
	work();
	for(i=1;i<=n+n;++i)a[i].x=-a[i].x;
	reverse(a+1,a+n+n+1);
	work();
	printf("%.10lf\n",ans/2);
}