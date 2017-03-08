#include<iostream>
#include<algorithm>
using namespace std;
int main(){
ios::sync_with_stdio(false);
int t,n,first,sec;
cin>>t;
while(t--){
    long int amount=0;
    first=0;sec=0;
    cin>>n;
    int cost[n];
    for(int i=0;i<n;i++){
        cin>>cost[i];
    }
    sort(cost,cost+n);
    if(n==1) cout<<cost[0]<<endl;
    else{
    for(int i=n-1;i>=0;i--){
        if(i>=0) first=cost[i];
        else first=0;
        i--;
        if(i>=0) sec=cost[i];
        else sec=0;
        amount+=first+sec;
        i-=2;
    }
    cout<<amount<<endl;
    }
}
}
