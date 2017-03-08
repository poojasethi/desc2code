#include<cstdio>
#include<algorithm>
using namespace std;
int x1[101],y1[101],x2[101],y2[101],u,a[101],n,w[101];
int main(){
  scanf("%d",&n);
  for(int i=0;i<n;i++){
  	scanf("%d%d%d%d",&x1[i],&y1[i],&x2[i],&y2[i]);
  	a[i] = abs(x2[i]-x1[i]); w[i] = a[i]*a[i]*a[i]; 
  }
  for(int i=1;i<n && !u;i++){
  	for(int j=i,x_all =0,y_all = 0,w_all=0; j>0 && !u;j--){
  		x_all += (x1[j]+x2[j])*w[j], y_all += (y1[j]+y2[j])*w[j];
  		w_all += w[j];
  		if(abs((x1[j-1]+x2[j-1])*w_all - x_all) > a[j-1]*w_all || abs((y1[j-1]+y2[j-1])*w_all - y_all) > a[j-1]*w_all){
  			u = 1; printf("%d\n",i);
  		} 
  	}
  }
  if(!u) printf("%d\n",n);
  return 0;
}