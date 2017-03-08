#include<iostream>
using namespace std;
int gcd(int,int);
int main(){
ios::sync_with_stdio(false);
int t,n,a,res;
cin>>t;
while(t--){
    cin>>n;
    res=0;
    for(int i=0;i<n;i++){
        cin>>a;
        res=gcd(res,a);
    }
    if(res==1) cout<<n<<endl;
    else cout<<"-1"<<endl;
}
}
int gcd(int x,int y){
if(y==0) return x;
else return gcd(y,x%y);
}

