#include<iostream>
using namespace std;
int main(){
ios::sync_with_stdio(false);
int n,q,rc,x;
string op;
cin>>n>>q;
long long int row[n],col[n];
long long int maxr=0,maxc=0;
for(int i=0;i<n;i++){
    row[i]=0;
    col[i]=0;
}
while(q--){
    cin>>op>>rc>>x;
    if(op=="RowAdd"){
        row[rc-1]+=x;
        maxr=max(maxr,row[rc-1]);
    }
    else if(op=="ColAdd"){
        col[rc-1]+=x;
        maxc=max(maxc,col[rc-1]);
    }
}
cout<<maxr+maxc<<endl;
}
