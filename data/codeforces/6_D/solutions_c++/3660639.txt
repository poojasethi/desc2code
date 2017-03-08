#include <cstdio>
#include <iostream>
using namespace std;
int n,a,b,ans=1;
int h[20],shoot[1000];
bool dfs(int l,int balls,int last){
    if(balls==0){
        for(int i=1;i<=n;i++)
            if(h[i]>=0)
                return false;
        return true;
    }
    if(h[l]<0)
        return dfs(l+1,balls,last);
    for(int i=min(n-1,max(last,max(2,l)));i<=min(n-1,l+1);i++){
        shoot[balls]=i;
        h[i]-=a;
        h[i-1]-=b;
        h[i+1]-=b;
        if(dfs(l, balls-1, i))
            return true;
        h[i]+=a;
        h[i-1]+=b;
        h[i+1]+=b;
    }
    return false;
}
int main(){
    cin>>n>>a>>b;
    for(int i=1;i<=n;i++)
        cin>>h[i];
    for(;ans;ans++){
        if(dfs(1,ans,2)){
            cout<<ans<<endl;
            for(int i=ans;i>=1;i--)
                cout<<shoot[i]<<' ';
            cout<<endl;
            return 0;
        }
    }
    return 0;
}