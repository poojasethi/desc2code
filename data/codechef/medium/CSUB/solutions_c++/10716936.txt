#include<iostream>
using namespace std;
int main(){
ios::sync_with_stdio(false);
long long int t,n,i,c;
unsigned long long int ans;
cin>>t;
string s;
while(t--){
    cin>>n;
    cin>>s;
    c=0;
    for(i=0;i<n;i++)
        if(s[i]=='1') c++;
    ans=(c*(c+1))/2;
    cout<<ans<<endl;
}
}
