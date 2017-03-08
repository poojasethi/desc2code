#include <iostream>
using namespace std;

int main(){
    long long p,d,a,i;
    cin>>p>>d;
    a=++p;
    for(i=10; ;i*=10){
        if(p%i>d) break;
        a=p-p%i;
    }
    cout<<a-1<<endl;
}