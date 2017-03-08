#include<iostream>
using namespace std;
int main(){
ios::sync_with_stdio(false);
int t,n,x,l,f;
cin>>t;
while(t--){
    cin>>n;
    int time=0,wait=0;
    for(int i=0;i<n;i++){
        cin>>x>>l>>f;
        wait=x;
        while(time>wait) wait+=f;
        wait=wait-time;
        time+=wait;
        time+=l;
    }
    cout<<time<<endl;
}
}
