#include <iostream>
using namespace std;

int main()
{ int s1,a; cin>>s1>>a;
int s=0;
while (a>0) {s=s*10+a%10; a/=10; }
cout<<s1+s;
return 0;
}