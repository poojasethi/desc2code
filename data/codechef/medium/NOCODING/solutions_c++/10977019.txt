#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define fora(i,N) for(int i=1;i<N;i++)
#define star ll T;cin>>T;while(T--)
int main(){
star{
    string str;
    cin>>str;
    ll i,count=2,N=str.size();
    fora(i,N){
                if(str[i]-str[i-1]<0){
                    count+=(27+str[i]-str[i-1]);
                }
                else{
                    count+=(str[i]-str[i-1]+1);
                }
    }
    if(11*N>=count){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
    cout<<endl;
}
return 0;
}
