#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#define ll long long
using namespace std;
const int maxn= 1e5+10,mo= 1e9+7,alpha= 26;
struct query{
	int x,y;
}Q[maxn];
char s[maxn];
int X[maxn],alpha_n[maxn],a_1n[maxn],c[maxn];
int sigma[500][maxn],M[maxn],inva[maxn],invc[maxn];
int n,m,len,i,j,x,y,tot,ans,q;
void gcd(int a,int b,int &x,int &y){
	if (!b){
		x= 1;
		y= 0;
		return;
	}gcd(b,a%b,x,y);
	int t= x;
	x= y;
	y= t-a/b*y;
}
void update(int len){
	int i,z;
	X[len]= ++tot;
	for (i= len;i<=M[len];i++){
		z= (ll)a_1n[i-len]*inva[i]%mo;
		z= (ll)z*c[i-1]%mo*invc[i-len]%mo*invc[len-1]%mo;
		z= (z+mo)%mo;
		sigma[tot][i]= (sigma[tot][i-1]+z)%mo;
	}	
}
int main()
{
#ifndef ONLINE_JUDGE	
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
#endif
	alpha_n[0]= 1;
	a_1n[0]= 1;
	c[0]= 1;
	for (i= 1;i<=1e5;i++){
		alpha_n[i]= (ll)alpha_n[i-1]*alpha%mo;
		a_1n[i]= (ll)a_1n[i-1]*(alpha-1)%mo;
		c[i]= (ll)c[i-1]*i%mo;
	}
	for (i= 0;i<=1e5;i++){
		gcd(alpha_n[i],mo,inva[i],y);
		gcd(c[i],mo,invc[i],y);
	}
	scanf("%d",&m);
	scanf("%s",s+1);
	len= strlen(s+1);
	for (int t= 1;t<=m;t++){
		scanf("%d",&x);
		if (x==1){
			scanf("%s",s+1);
			len= strlen(s+1);
		}else {
			scanf("%d",&x);
			Q[++q]= (query){x,len};
			M[len]= max(M[len],x);
		}		
	}
	for (i= 1;i<=q;i++){
		x= Q[i].x;
		len= Q[i].y;
		if (!X[len]) update(len);
		ans= (ll)alpha_n[x]*sigma[X[len]][x]%mo;
		printf("%d\n",ans);		
	}
	/*update(len);
	for (int t= 1;t<=m;t++){
		scanf("%d",&x);
		if (x==1){
			scanf("%s",s+1);
			len= strlen(s+1);
			if (!X[len])
				update(len);			
		}else {
			scanf("%d",&x);
			ans= (ll)alpha_n[x]*sigma[X[len]][x]%mo;
			printf("%d\n",ans);
		}
		}*/
	return 0;
}
