#include<iostream>
using namespace std;
int main(){
ios::sync_with_stdio(false);
int t;
long long int n;
cin>>t;
while(t--){
    cin>>n;
    long long int maxv=0,pos;
    long long int w;
    for(int i=0;i<n;i++){
        cin>>w;
        w+=i;
        if(w>maxv){
            maxv=w;
            pos=i;
        }
    }
    cout<<maxv<<endl;
}
}
