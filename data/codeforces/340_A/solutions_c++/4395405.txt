#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int x,y,a,b;
    cin>>x>>y>>a>>b;
    int lcm=(x*y)/__gcd(x,y);
    cout<<b/lcm-(a-1)/lcm<<endl;
    return 0;
}
