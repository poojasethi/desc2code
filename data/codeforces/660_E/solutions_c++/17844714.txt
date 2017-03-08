#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<cmath>
#define ll long long
#define ld long double
using namespace std;
const int maxn= 1e6+10,mo= 1e9+7,MM= 1e6;
int c[maxn],M_1[maxn],M[maxn],invc[maxn];
int n,m,i,j,k,s,ans,x;
int comb(int m,int n){
	return (ll)c[m]*invc[m-n]%mo*invc[n]%mo;
}
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
int main()
{
#ifndef ONLINE_JUDGE	
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
#endif
	scanf("%d%d",&n, &m);
	c[0]= M_1[0]= M[0]= 1;
	for (i= 1;i<=MM;i++){
		c[i]= (ll)c[i-1]*i%mo;
		M_1[i]= (ll)M_1[i-1]*(m-1)%mo;
		M[i]= (ll)M[i-1]*m%mo;
	}
	for (i= 0;i<=MM;i++)
		gcd(c[i],mo,invc[i],x);
	for (s= 0;s<=n-1;s++){
		ans+= (ll)M_1[s]*M[n-s]%mo*comb(n,n-s-1)%mo;
		ans%= mo;
	}
	ans= ((ans+M[n])%mo+mo)%mo;
	printf("%d",ans);
	return 0;
}
