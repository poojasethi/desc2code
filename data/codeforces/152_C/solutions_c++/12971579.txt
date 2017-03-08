#include <bits/stdc++.h>
using namespace std ;
const int mod1 = 1000000007;
int main()
{	
	int n,m;
    char a[100][105];
    cin >> n >> m ;
    set<char> u[100];
    for(int i=0;i<n;i++)
    {
        cin >> a[i] ;
        for(int j=0;j<m;j++) 
        	u[j].insert(a[i][j]);
    }
    long long int ans=1;
    for(int i=0;i<m;i++) 
    	ans=(ans*u[i].size())%mod1;
    cout << ans ;
	return 0 ;
}