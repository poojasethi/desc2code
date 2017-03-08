#include<bits/stdc++.h>

using namespace std;
#define ll long long
#define beg ll T; cin>>T; while(T--)


int main(){
    beg{
        ll N,sum=0;
        cin>>N;
        int A[6]={1,2,5,10,50,100};
        for(ll i=5;i>=0;i--){
            sum=sum+(N/A[i]);
            N%=A[i];
        }
        cout<<sum<<endl;
        }
return 0;
}
