#include<iostream>
using namespace std;

int main(){
int n,m;
cin>>n>>m;
int a[101] = {0};
int b[101] = {0};
int aa,bb,cc;
while(m--){
cin>>aa>>bb>>cc;
a[aa] += cc;
b[bb] += cc;
}
int res = 0;
for(int i = 1 ; i <= n ; i++){
if(a[i] > b[i])
res+=(a[i]-b[i]);
}
cout<<res<<endl;
return 0;
}
