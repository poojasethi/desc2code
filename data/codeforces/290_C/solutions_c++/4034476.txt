#include <iostream>
#include <algorithm>
    using namespace std;
int main(){
    int n;
    float z,y=0,maxi=0;
    cin>>n;
    for(int a=1;a<=n;a++){
    cin>>z;
    y+=z;
    maxi=max(maxi,y/a);
    }
    cout<<maxi<<endl;
    return 0;
}