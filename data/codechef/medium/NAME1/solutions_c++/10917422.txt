#include<iostream>
#include<cstring>
using namespace std;
int main(){
ios::sync_with_stdio(false);
int t,n;
cin>>t;
while(t--){
    char a[40007],b[40007];
    cin>>a>>b;
    int flag=0;
    int parent[27]={0};
    for(int i=0;i<strlen(a);i++){
        parent[a[i]-'a']++;
    }
    for(int i=0;i<strlen(b);i++){
        parent[b[i]-'a']++;
    }
    cin>>n;
    char c[40007];
    for(int i=0;i<n;i++){
        cin>>c;
        for(int j=0;j<strlen(c);j++){
            parent[c[j]-'a']--;
        }
    }
    for(int i=0;i<27;i++){
        if(parent[i]<0){
            flag=1;
            break;
        }
    }
    if(flag==0) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
}
}
