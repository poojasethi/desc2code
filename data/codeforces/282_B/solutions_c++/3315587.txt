#include<iostream>
using namespace std;
int n;
int a,b,suma,sumb;
int main()
{
    cin>>n;
    while(n--)
    {
        cin>>a>>b;
        if(suma+a<=sumb+500)cout<<"A",suma+=a;
        else sumb+=b,cout<<"G";
    }cout<<endl;
}
