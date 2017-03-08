#include<iostream>
#include<algorithm>
using namespace std;
int main(){
ios::sync_with_stdio(false);
long long int n,d,i,c=0;
cin>>n>>d;
long long int l[n];
for(i=0;i<n;i++){
    cin>>l[i];
}
sort(l,l+n);
for(i=0;i<n-1;i++){
    if(l[i+1]-l[i]<=d){
        c++;
        i+=1;
    }
}
cout<<c<<endl;
}
