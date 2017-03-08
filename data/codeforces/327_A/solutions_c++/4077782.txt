#include<iostream>
using namespace std;
int n,t,a[101],s=0;
int main(){
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>t;
        s+=t;
        t?t=-1:t=1;
        a[i]=max(t,a[i-1]+t);
        a[0]=max(a[0],a[i]);
    }
    cout<<a[0]+s-(s==n);
}
