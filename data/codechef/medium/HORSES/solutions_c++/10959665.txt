#include<bits/stdc++.h>
using namespace std;

/* Template by Mohit Kumra
mohitkumra95@gmail.com */

#define mod 1000000007
#define ll long long
#define vll vector<ll>
#define vstr vector<str>
#define pb push_back
#define mpll map<ll,ll>
#define mplstr map<ll,str>
#define prll pair<ll,ll>
#define prlch pair<ll,ch>
#define fr first
#define sc second
#define fora(i,N) for(int i=0;i<N;i++)
#define ford(i,N) for(int i=N-1;i>=0;i--)
#define star ll T;cin>>T;while(T--)


int main(){
star{
    ll N,i;
    cin>>N;
    ll A[N],diff=mod;
    fora(i,N){
        cin>>A[i];
    }
    sort(A,A+N);
    N-=1;
    fora(i,N){
        if(A[i+1]-A[i]<diff){
            diff=A[i+1]-A[i];
        }
    }
    cout<<diff<<endl;
}
return 0;
}
