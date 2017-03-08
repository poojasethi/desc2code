#include<iostream>
#include<string>
using namespace std;
int main(){
int k,n,good=0;
size_t found;
cin>>k>>n;
string a[k];
string b;
for(int i=0;i<k;i++){
    cin>>a[i];
}
for(int i=0;i<n;i++){
    good=0;
    cin>>b;
    if(b.length()>=47){
        good=1;
    }
    else{
        for(int j=0;j<k;j++){
            found = b.find(a[j]);
            if (found!=string::npos){
                good=1;
                break;
            }
        }
    }
    if(good==1) cout<<"Good"<<endl;
    else cout<<"Bad"<<endl;
}
}
