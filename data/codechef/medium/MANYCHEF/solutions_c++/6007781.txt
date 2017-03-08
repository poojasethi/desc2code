#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        char a[2014];
        cin>>a;
        for(int i = strlen(a)-1;i>=0;i--){
            if((a[i]=='F'||a[i]=='?')&&(a[i-1]=='E'||a[i-1]=='?')&&(a[i-2]=='H'||a[i-2]=='?')&&(a[i-3]=='C'||a[i-3]=='?')){
                a[i]='F';
                a[i-1]='E';
                a[i-2]='H';
                a[i-3]='C';
            }else if(a[i]=='?'){
                a[i]='A';
            }
        }
        cout<<a<<endl;
        t--;
    }
    return 0;
}
