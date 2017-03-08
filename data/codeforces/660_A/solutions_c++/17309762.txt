#include<bits/stdc++.h>
using namespace  std;
int main(){
    int n,k=0; cin >> n; int arr[n]; for(int i=0;i<n;i++) cin >> arr[i];
    vector<int> A;A.push_back(arr[0]);
    for(int i=1;i<n;i++){
        if(__gcd(arr[i],arr[i-1])>1 ) { ++k;A.push_back(1); }//push right element
        A.push_back(arr[i]);
    }
    cout<<k<<endl;
    for(int i=0;i<A.size();i++) cout<<A[i]<<" "; cout<<endl;
    return 0;
}
