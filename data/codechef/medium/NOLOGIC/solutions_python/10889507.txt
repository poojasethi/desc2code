#include<iostream>
#include<ctype.h>
#include<string>
#include<string.h>
#include<stdio.h>
using namespace std;
int main(){
int t,c;
char logic[315];
cin>>t;
getchar();
while(t--){
    gets(logic);
    int ascii[127]={0};
    int c=0;
    int len=strlen(logic);
    for(int i=0;i<len;i++) logic[i]=tolower(logic[i]);
    for(int i=0;i<len;i++) ascii[logic[i]]++;
    for(int i=97;i<=122;i++){
        if(ascii[i]==0){
            char out=i;
            cout<<out;
            c++;
        }
    }
    if(c==0) cout<<"~"<<endl;
    else cout<<endl;
}
}
