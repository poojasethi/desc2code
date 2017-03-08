#include <bits/stdc++.h>
using namespace std ;
int ans,n ;
void res(int x) 
{
    if(x > n) 
    	return;
    ans++;
    res(x*10);
    res(x*10+1);
}
int main()
{
    cin >> n ;
    ans = 0;
    res(1);
    cout << ans ;
}