#include <bits/stdc++.h>
using namespace std;
#define f(s,a) for(int i=0;i<s;i++) cin>>a[i];
int main() {
  int n,m,c,a[1000],b[1000];cin>>n;f(n,a)cin>>m;f(m,b)sort(a,a+n);sort(b,b+m);for(int i=0,j=0;i<n && j<m;)if(a[i]-1>b[j]) j++;else if(a[i]<b[j]-1) i++;else c++,i++,j++;
  cout<<c;}