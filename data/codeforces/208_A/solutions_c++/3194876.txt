#include<iostream>
#include<string>
using namespace std;
string a,b;
int c;
int main(){
cin>>a;
c=a.find("WUB");
while( c!=-1){
    a.replace(c,3," ");
    c=a.find("WUB");
}
cout << a << endl;
}