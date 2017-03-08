#include<bits/stdc++.h>

using namespace std;

int main(){
    int a,b,maxi=0;
    cin>>a>>b;
    int temp=a;
    while(temp){
        maxi=max(maxi,temp%10);
        temp/=10;
    }
    temp=b;
    while(temp){
        maxi=max(maxi,temp%10);
        temp/=10;
    }
    maxi++;
    int carry=0,len=0,sum;
    while(a || b || carry){
        sum=(a%10)+(b%10)+carry;
        carry=sum/maxi;
        len++;
        a/=10;
        b/=10;
    }
    cout<<len<<endl;
    return 0;
}
