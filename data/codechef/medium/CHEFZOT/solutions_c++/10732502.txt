#include<iostream>
using namespace std;
int main(){
ios::sync_with_stdio(false);
int n,c;
cin>>n;
int a[n];
c=0;
int flag=0;
int maxm=0;
for(int i=0;i<n;i++){
    cin>>a[i];
}
for(int i=0;i<n;i++){
    if(a[i]!=0) c++;
    else if(a[i]==0){
        if(c>maxm) maxm=c;
        c=0;
        flag=1;
    }
}
if(c>maxm) maxm=c;
if(flag==0) cout<<n<<endl;
else cout<<maxm<<endl;
}
