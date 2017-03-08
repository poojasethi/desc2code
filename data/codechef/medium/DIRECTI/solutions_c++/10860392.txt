#include<bits/stdc++.h>
using namespace std;
int main(){
int t,n;
cin>>t;
while(t--){
    cin>>n;
    int data[n];
    string dir,on;
    char place[n][100];
    getchar();
    for(int i=0;i<n;i++){
        cin>>dir>>on;
        getchar();
        gets(place[i]);
        if(dir=="Begin") data[i]=0;
        else if(dir=="Left") data[i]=1;
        else if(dir=="Right") data[i]=2;
    }
    cout<<"Begin on "<<place[n-1]<<endl;
    for(int j=n-2;j>=0;j--){
        if(data[j+1]==1) dir="Right";
        else if(data[j+1]==2) dir="Left";
        cout<<dir<<" on "<<place[j]<<endl;
    }
}
}
