#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
#define N 10050
#define ll long long
ll t[N],LCM,pos,n,m,p;
inline ll Read()
 {
 	ll x=0;char y;
 	do y=getchar(); while (y<'0'||y>'9');
 	do x=x*10+y-'0',y=getchar(); while (y>='0'&&y<='9');
 	return x;
 }
ll gcd(ll x,ll y)
 {return !y?x:gcd(y,x%y);}
ll exgcd(ll a,ll b,ll &x,ll &y)
 {
 	if (!b) {x=1;y=0;return a;}
 	ll k=exgcd(b,a%b,y,x);
 	y-=a/b*x;return k;
 }
bool Solve()
 {
 	LCM=t[1];pos=0;
    if (LCM>n) return false;
    for (int i=2;i<=p;i++)
     {
     	ll now=1-i,x,y,k=exgcd(LCM,t[i],x,y);
     	if ((pos-now)%k||n/LCM<t[i]/k) return false;
     	pos+=LCM*((now-pos)/k%t[i]*x%t[i]);
     	pos%=LCM*=t[i]/k;
     }
    pos+=pos<=0?LCM:0;
    if (pos+p-1>m) return false;
    for (int i=1;i<=p;i++)
     if (gcd(LCM,pos+i-1)!=t[i]) return false;
    return true;
 }
int main()
 {
 	n=Read();m=Read();p=Read();
 	for (int i=1;i<=p;i++) t[i]=Read();
 	if (Solve()) puts("YES"); else puts("NO");
 	return 0;
 }