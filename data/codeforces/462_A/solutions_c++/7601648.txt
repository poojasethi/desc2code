#include<bits/stdc++.h>
using namespace std;

bool a[102][102];
int n,i,j;
string s;

int main()
{
    cin>>n;
    for(i=1;i<=n;i++)
    {
        cin>>s;
        for(j=0;s[j]!='\0';j++)
            a[i][j+1]=(s[j]=='o');
    }
    for(i=1;i<=n;i++)
    for(j=1;j<=n;j++)
    if((a[i-1][j]+a[i+1][j]+a[i][j-1]+a[i][j+1])&1) { cout<<"NO";return 0; }
    cout<<"YES";
    return 0;
}
