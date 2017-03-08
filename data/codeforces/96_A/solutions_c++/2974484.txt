#include<iostream>
#include<string>
using namespace std;
int main(){
string x;
cin>>x;
if(x.find("1111111")==-1&&x.find("0000000")==-1)
cout<<"NO";
else cout<<"YES";
return 0;
}