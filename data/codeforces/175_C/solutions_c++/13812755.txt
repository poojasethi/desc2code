#include<bits/stdc++.h>
#include<vector>
using namespace std;
#define ll long long int
#define pi pair<ll,ll>
#define f first
#define s second
#define mp make_pair
bool func(pi a,pi b){
return (a.s<b.s);
}
int main(){
ll n;
cin>>n;
pi a[n];
for(int i=0;i<n;i++){
cin>>a[i].f>>a[i].s;
}
sort(a,a+n,func);
ll t;
cin>>t;
ll p[t];
for(int i=0;i<t;i++) cin>>p[i];
ll ans=0;
ll fac=1;
ll cur=0;
int j=0;
int i;
for(i=0;i<t;i++){
while(cur+a[j].f<=p[i]){
cur=cur+a[j].f;
ans=ans+(a[j].f*(i+1)*a[j].s);
j++;
if(j==n) break;
}
if(j==n) break;
ans=ans+((p[i]-cur)*(i+1)*a[j].s);
a[j].f=a[j].f-p[i]+cur;
cur=p[i];
}
while(j!=n){
ans=ans+(a[j].f*(t+1)*a[j].s);
j++;
}
cout<<ans;
}