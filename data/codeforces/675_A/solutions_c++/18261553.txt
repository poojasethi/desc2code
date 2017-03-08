#include <bits/stdc++.h>

using namespace std;
bool fn(){
long long a,b,c;
cin>>a>>b>>c;
if(c==0) return a==b;
if((b-a)%c!=0) return false;
return (b-a)/c>=0;

}

int main()
{
    puts(fn() ? "YES" : "NO");
}
