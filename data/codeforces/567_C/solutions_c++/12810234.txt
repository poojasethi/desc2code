#include<bits/stdc++.h>
using namespace std;
#define ll long long
map<ll,ll> m,o;ll s,n,k,a,i;
int main(){cin>>n>>k;for(i=0;i<n;i++){cin>>a;if (a%k==0) {s+=m[a/k];m[a]+=o[a/k];}o[a]++;}cout<<s;}
