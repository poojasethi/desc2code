#include<bits/stdc++.h>

using namespace std;
#define ll long long
#define beg ll T; cin>>T; while(T--)

int main(){
    beg{
        ll N;
        cin>>N;
        ll A[N];
        for(ll i=0;i<N;i++){
            cin>>A[i];
        }
        sort(A,A+N);
        cout<<A[0]+A[1]<<endl;
}
return 0;
}
