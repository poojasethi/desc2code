#include<iostream>
using namespace std;
int main(){
ios::sync_with_stdio(false);
int t,n,k,a;
cin>>t;
while(t--){
    cin>>n>>k;
    int c=0;
    for(int i=0;i<n;i++){
        cin>>a;
        if(a%2==0) c++;
    }
    if(k==0){
        if(c==n) cout<<"NO"<<endl;
        else cout<<"YES"<<endl;
    }
    else if(k>0){
        if(c>=k) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
}
}
