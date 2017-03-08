#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<bitset>
#define cl(a) memset(a,0,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
const db pi=3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862;
void gn(int &x){
    int sg=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');
    if(c=='-')sg=-1,x=0;else x=c-'0';
    while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';
    x*=sg;
}
void gn(ll &x){
    int sg=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');
    if(c=='-')sg=-1,x=0;else x=c-'0';
    while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';
    x*=sg;
}
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
#define x1 x192837465
#define x2 x123456789
#define y1 y192837465
#define y2 y123456789
inline ll gcd(ll a,ll b){return b?gcd(b,a%b):a;}
inline ll mul(ll a,ll b,ll mo)  
{  
	a%=mo,b%=mo;
	if(a<0)a+=mo;if(b<0)b+=mo;
	if(mo<=2e9)return a*b%mo;
	return ((a*b-(ll)((long double)a/mo*b)*mo)%mo+mo)%mo;  
	/*ll ans=0;
	do{
		if(b&1)ans=(ans+a)%mo;
		a=(a+a)%mo;
	}while(b>>=1);
	return ans;*/
}  
inline ll qp(ll a,ll b,ll mo){
	ll ans=1;
	do{
		if(b&1)ans=mul(ans,a,mo);
		a=mul(a,a,mo);
	}while(b>>=1);
	return ans;
}
char N[111111];
ll n;
inline ll getn(ll mo){
	unsigned long long ans=0;
	for (int i=0;N[i];i++){
		ans=(ans*10+N[i]-'0')%mo;
	}
	return ans;
}
ll mo,q;
ll m1,m2,m3;
int d;
ll p[22222];
ll inv[22222];
ll fac[22222],ifac[22222];

ll exgcd(ll a,ll b,ll&lx,ll&ly){
    ll x=0,y=1,q,t;lx=1,ly=0;
    while(b){
    	q=a/b;
        t=b;b=a%b;a=t;
        t=x;x=lx-q*x;lx=t;
        t=y;y=ly-q*y;ly=t;
    }
    return a;
}
ll getinv(ll a,ll mo){
	ll ans,tmp;
	exgcd(a,mo,ans,tmp);
	if(ans<0)ans+=mo;
	return ans;
}

ll lag(ll *p,ll n,int d){
	ll ans=0;
	static ll pre[22222],suc[22222];
	pre[0]=suc[d]=1;
	for (int i=1;i<=d;i++)pre[i]=mul(pre[i-1],n-(i-1),mo);
	for (int i=d-1;i>=0;i--)suc[i]=mul(suc[i+1],n-(i+1),mo);
	for (int j=0;j<=d;j++){
		ll tmp=p[j];
		if((d-j)&1)tmp*=-1;
		tmp=mul(tmp,pre[j],mo);
		tmp=mul(tmp,suc[j],mo);
		tmp=mul(tmp,ifac[j],mo);
		tmp=mul(tmp,ifac[d-j],mo);
		ans=(ans+tmp)%mo;
	}
	return (ans+mo)%mo;
}

ll a1,a2,a3;
ll work1(){
	if(d<100){
		for (int i=d+1;i<=100;i++)p[i]=lag(p,i,d)%m1;
	}
	ll ans=0;
	ll qq=1;
	ll n=0;
	for (int i=0;N[i];i++){
		n=n*10+N[i]-'0';
		if(n>100){
			n=100;
			break;
		}
	}
	for (int i=0;i<min(n,100ll);i++){
		ans=(ans+mul(p[i],qq,m1))%m1;
		qq=mul(qq,q,m1);
	}
	return (ans+m1)%m1;
}
ll work2(){
	for (int i=d+1;i<=d+14;i++)p[i]=lag(p,i,d);
	static ll su[22222];
	su[0]=0;
	ll qq=1;
	for (int i=1;i<=d+14;i++){
		su[i]=(su[i-1]+mul(p[i-1],qq,m2))%m2;
		qq=mul(qq,q,m2);
	}
	ll ans=(lag(su,n,d+14)%m2+m2)%m2;
	return ans;
}
ll work3(){
	static ll k[22222],b[22222];
	k[0]=1;b[0]=0;
	ll iq=getinv(q,m3);
	for (int i=1;i<=d+1;i++){
		k[i]=mul(iq,k[i-1],m3);
		b[i]=mul(iq,(b[i-1]+p[i-1])%m3,m3);
	}
	ll suk=0,sub=0;
	for (int i=0;i<=d+1;i++){
		ll tmp=mul(mul(fac[d+1],ifac[d+1-i],m3),ifac[i],m3);
		if(i&1)tmp*=-1;
		suk=(suk+mul(tmp,k[i],m3))%m3;
		sub=(sub+mul(tmp,b[i],m3))%m3;
	}
	ll x=(-mul(sub,getinv(suk,m3),m3))+m3;

	ll f[22222];
	for (int i=0;i<=d;i++){
		f[i]=(mul(x,k[i],m3)+b[i])%m3;
	}
	ll ret=((lag(f,n,d))%m3+m3)%m3;
	ll pr=1;
	ll rec[10];
	rec[0]=1;
	for (int i=1;i<=9;i++)rec[i]=mul(rec[i-1],q,m3);
	for (int i=0;N[i];i++){
		int d=N[i]-'0';
		pr=qp(pr,10,m3);
		pr=mul(pr,rec[d],m3);
	}
	ret=mul(ret,pr,m3);
	ret-=f[0];
	return ((ret%m3)+m3)%m3;
}

void crt(ll a,ll n,ll b,ll m,ll &c){
	ll in=mul(getinv(n,m),b-a,m);
	ll ret=(a+mul(n,in,m*n))%(m*n);
	c=ret;
}
ll work(){
	if(q==0)return p[0];
	else if(q==1){
		static ll su[22222];
		su[0]=0;
		for (int i=1;i<=d+1;i++)su[i]=(su[i-1]+p[i-1])%mo;
		ll ans=lag(su,n,d+1);
		return ans;
	}else{
		ll tmp=mo;
		ll t;
		m1=m2=m3=1;
		while((t=gcd(tmp,q))!=1){
			m1*=t;
			tmp/=t;
		}
		while((t=gcd(tmp,q-1))!=1){
			m2*=t;
			tmp/=t;
		}
		m3=mo/m1/m2;
		ll a1=work1();
		ll a2=work2();
		ll a3=work3();

		ll a4,a5;
		crt(a1,m1,a2,m2,a4);
		crt(a3,m3,a4,m1*m2,a5);
		return (a5%mo+mo)%mo;
	}
}
int main()
{
	int tes;
	gn(tes);
	while(tes--){
		gn(mo);
		gn(q);
		scanf("%s",N);
		n=getn(mo);
		gn(d);
		for (int i=0;i<=d;i++)gn(p[i]);
		inv[1]=1;
		for (int i=2;i<=d+14;i++)inv[i]=mul(inv[mo%i],-(mo/i),mo);
		fac[0]=ifac[0]=1;
		for (int i=1;i<=d+14;i++)fac[i]=mul(fac[i-1],i,mo),ifac[i]=mul(ifac[i-1],inv[i],mo);
		printf("%lld\n",work());
	}
	return 0;
}
