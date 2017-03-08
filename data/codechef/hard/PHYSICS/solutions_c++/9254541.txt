#include<iostream>
#include<math.h>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<cstring>
#define M 1000000007
#define ll long long int

using namespace std;

int a[10002];
int main(){
int t,n,f,i,h;
cin>>t;
while(t--){
    cin>>n>>f;
    for(i=0;i<n;i++){
        cin>>h;
        while(h%f==0){
            h/=f;
        }
        a[i]=h;
    }
    sort(a,a+n);
    int cnt=1,ans=0,temp=a[0];
    for(i=1;i<n;i++){
        if(temp!=a[i]){
            temp=a[i];
            cnt=0;
        }
        ans+=cnt;
        cnt++;
    }
    cout<<ans<<endl;
}
return 0;
}
