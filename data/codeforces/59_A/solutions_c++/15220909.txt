#include <bits/stdc++.h>
using namespace std;
int main()
{
    char a[110];
    int up=0,lo=0;
    cin>>a;
    for(int i=0;a[i]!=NULL;i++){(isupper(a[i]))?up++:lo++;}
    (up>lo)?cout<<strupr(a):cout<<strlwr(a);
    return 0;
}